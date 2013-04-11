import urllib2
import json
import sublime, sublime_plugin
import os

class HtmlToHamlFromFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		source = self.view.file_name()
		if source.endswith(".erb"):
			target = source.replace('.erb', '.haml')
		if source.endswith(".html"):
			target = source + '.haml'
		if target:
			with open(source, 'r') as f:
				html = f.read()
			haml = HTHTools.convert_html_to_haml(html)
			if haml != None:
				with open(target, 'w') as f:
					f.write(haml)
				self.view.window().open_file(target)

	def is_enabled(self):
		return True #return (self.view.file_name().endswith(".html") or self.view.file_name().endswith(".erb"))

class HtmlToHamlFromSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				html = self.view.substr(region)
				haml = HTHTools.convert_html_to_haml(html)
				if haml != None:
					self.view.replace(edit, region, haml)

	def is_enabled(self):
		return True #return self.view.file_name().endswith(".haml")

class HtmlToHamlFromClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		html = sublime.get_clipboard()
		haml = HTHTools.convert_html_to_haml(html)
		if haml != None:
			for region in self.view.sel():
				self.view.replace(edit, region, haml)

	def is_enabled(self):
		return True #return self.view.file_name().endswith(".haml")

class HTHTools:
	@classmethod
	def post_html_return_haml(self, html):
		host = 'http://html2haml.heroku.com/api.json'
		data = {'page': {'html': html}}
		data_json = json.dumps(data)
		req = urllib2.Request(host, data_json, {'content-type': 'application/json'})
		response_stream = urllib2.urlopen(req)
		result = json.loads(response_stream.read())

		if result["page"]:
			return result["page"]["haml"]
		else:
			return None

	@classmethod
	def local_html2haml(self, html):
		from subprocess import Popen, PIPE
		child = Popen('echo "'+ html +'" | html2haml -s', shell=True, stdout=PIPE)
		haml = child.communicate()[0]
		return_code = child.returncode
		if os.WEXITSTATUS(return_code) == 0:
			return haml
		else:
			return None

	@classmethod
	def convert_html_to_haml(self, html):
		if os.WEXITSTATUS(os.system('which html2haml')) == 0: #if local html2haml is available
			return self.local_html2haml(html)
		else:
			return self.post_html_return_haml(html)