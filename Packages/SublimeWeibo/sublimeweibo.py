import sublime, sublime_plugin
from aweibo import weibo

wb = weibo()

def show_in_file(text, syntax = 'Packages/JavaScript/JSON.tmLanguage'):
	tmpview = sublime.active_window().new_file()
	if syntax:
		tmpview.set_syntax_file(syntax)
	edit = tmpview.begin_edit()
	tmpview.insert(edit, 0, text)
	tmpview.set_read_only(True)
	tmpview.end_edit()

class WeiboaccessCommand(sublime_plugin.WindowCommand):
	def run(self):
		wb.get_token()

class WeibosendCommand(sublime_plugin.WindowCommand):
	def run(self, text = ''):
		self.window.show_input_panel('Input your status here: ', text, self.on_done, self.on_change, None)

	def on_done(self, text):
		if 0 < len(text) <= 140:
			wb.send(text)
		elif len(text) > 140:
			self.run(text)
			sublime.error_message("140+")			

	def on_change(self, text):
		sublime.status_message(str(140 - len(text)) + ' letters left.')

class WeibogettimelineCommand(sublime_plugin.WindowCommand):
	def run(self):
		statuses = wb.get_timlines(True)
		if statuses and statuses != '{}':
			show_in_file(statuses)

class WeibogetatmeCommand(sublime_plugin.WindowCommand):
	def run(self):
		statuses = wb.get_at_me(True)
		if statuses and statuses != '{}':
			show_in_file(statuses)

class WeibocommentsCommand(sublime_plugin.WindowCommand):
	def run(self):
		statuses = wb.get_to_me(True)
		if statuses and statuses != '{}':
			show_in_file(statuses)
