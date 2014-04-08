import sublime, sublime_plugin
import re, types

class PhpDebugHelperCommand(sublime_plugin.TextCommand):
	matchObj = []
	direction = None
	function = None
	hasSpace = None
	markLineNum = []

	def run(self, edit, **args):
		"""Entry point"""
		v = self.view
		if args['cmd'] == 'clear':
			self.function = args['function']
			self.clear(v)
			return
		if args['cmd'] == 'show':
			self.markLineNum = []
			self.function = args['function']
			self.show(v)
			return
		self.direction = args['cmd']
		self.function = args['function']
		word = re.escape(v.substr(v.word(v.sel()[0])))
		string = v.substr(v.line(v.sel()[0]))
		self.hasSpace = True
		if re.match(r'\s', string) == None:
			self.hasSpace = False
		self.matchObj = re.findall(r'\$'+word, string)
		self.matchObj.extend(re.findall(r'\$'+word+'\[.*\]', string))
		self.matchObj.extend(re.findall(r'(\$[\w\d\->_\'"\[\]]+'+word+'[\$\[\]\'"\w\d_]*)', string))
		self.matchObj = list(set(self.matchObj))
		for x in self.matchObj:
			if x[0] != '$':
				self.matchObj.remove(x)
		if len(self.matchObj) > 1:
			v.window().show_quick_panel(self.matchObj, self.process)
		else:
			self.process(0)

	def process(self, variable = None):
		v = self.view
		if variable == -1:
			return
		if len(self.matchObj) >= 1:
			variable = self.matchObj[variable]
			variable = self.function+'('+variable+');'
			variable = variable.replace('$', '\$')
		else:
			variable = self.function+'();'

		if self.direction == 'prepend':
			v.run_command('move', {"by": "lines", "forward": False})

		v.run_command('move_to', {'to': 'eol'})
		if self.hasSpace == False:
			v.run_command('insert_snippet', {'contents': "\n"})
			v.run_command('insert_snippet', {'contents': variable})
		else:
			v.run_command('run_macro_file', {"file": "Packages/Default/Add Line in Braces.sublime-macro"})
			v.run_command('insert_snippet', {'contents': variable})
			v.run_command('move', {"by": "lines", "forward": True})
			v.run_command('run_macro_file', {"file": "Packages/Default/Delete Line.sublime-macro"})
			v.run_command('move', {"by": "lines", "forward": False})
			v.run_command('move_to', {'to': 'eol'})
		if len(self.matchObj) < 1:
			v.run_command('move', {"by": "characters", "forward": False})
			v.run_command('move', {"by": "characters", "forward": False})

	def clear(self, v):
		filehandler = open(v.file_name(), 'r')
		lines = filehandler.readlines()
		filehandler.close()
		filehandler = open(v.file_name(), 'w')
		for line in lines:
			isW = True
			for fun in self.function:
				if re.search(fun, line) != None:
					isW = False
					break
			if isW:
				filehandler.writelines(line)
		filehandler.close()
		v.window().show_quick_panel(['File has been change, auto reload!'], self.reloadFile)

	def reloadFile():
		pass

	def show(self, v):
		filehandler = open(v.file_name(), 'r')
		lines = filehandler.readlines()
		markList = []
		lineNum = 1
		for line in lines:
			for fun in self.function:
				if re.search(fun, line) != None:
					markId = line.strip()
					self.markLineNum.append(lineNum)
					markList.append('Line '+str(lineNum)+': '+markId)
					break
			lineNum = lineNum + 1
		filehandler.close()
		v.window().show_quick_panel(markList, self.goto)

	def goto(self, index):
		if index == -1:
			return
		self.view.run_command("goto_line", {"line": self.markLineNum[index]})