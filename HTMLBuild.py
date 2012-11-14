import sublime
import sublime_plugin
import webbrowser


class HtmlBuild(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        if not view:
            return
        file_name = view.file_name()
        webbrowser.open("file://" + file_name)
