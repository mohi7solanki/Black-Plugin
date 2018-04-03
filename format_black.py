import os

import sublime_plugin


class BlackCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        self.view.run_command("save")
        file_path = self.view.file_name()
        os.system('black {}'.format(file_path))
