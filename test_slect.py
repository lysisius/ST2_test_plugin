"""
a practice plugin for my learning
"""

import sublime, sublime_plugin

class TestSelectCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        braces = False
        # sels is a list of references of selections
        sels = self.view.sel()
        for sel in sels:
            # self.view.insert(edit, 0, self.view.substr(sel))
            # substr converts the ref into a string
            # string.find
            if self.view.substr(sel).find('{') != -1:
                braces = True

        if not braces:
            new_sels = []
            for sel in sels:
                # view.find returns the first region matched or None
                # end() is the last of the selected text, not the end of
                # the selection, for a selection can be a 'reverse' one
                sel2 = self.view.find('\}', sel.end())

                # basically, the sel2 is just the '\}'
                new_sels.append(sel2)
            # removes all regions
            sels.clear()

            # update the current selection references so that they point to 
            # '\}'
            for sel in new_sels:
                sels.add(sel)

            # this expands all the current selections to the bracket
            self.view.run_command("expand_selection", {"to": "brackets"})
