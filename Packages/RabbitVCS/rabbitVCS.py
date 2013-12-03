import sublime
import subprocess
import sublime_plugin

def _runcommand(command, path):
	handle = subprocess.Popen('svn info ' + path, stdout=subprocess.PIPE, shell=True)
	if handle.stdout.read() == '':
		sublime.error_message(''.join(['Unknown Error\n', 'Perhaps, ' + path, ' is not a working copy, plz check again']))
	else:
		subprocess.call('rabbitvcs ' + command + " " + path, shell = True)	

class rabbitUpCommand(sublime_plugin.TextCommand):
	def run(self, path=''):
		_runcommand("update", self.view.file_name())		

class rabbitCommitCommand(sublime_plugin.TextCommand):
	def run(self, path=''):		
		_runcommand("commit", self.view.file_name())

class rabbitLogCommand(sublime_plugin.TextCommand):
	def run(self, path=''):
		_runcommand("log", self.view.file_name())		

class rabbitAddCommand(sublime_plugin.TextCommand):
	def run(self, path=''):
		_runcommand("add", self.view.file_name())				

class rabbitDelCommand(sublime_plugin.TextCommand):
	def run(self, path=''):
		_runcommand("delete", self.view.file_name())	