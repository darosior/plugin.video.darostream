# coding: utf-8
import sys
import xbmcgui
import xbmcplugin


class App:
    def __init__(self, base_url, proc_id, query=''):
        self.base_url = base_url
        self.proc_id = int(proc_id)
        self.query = query

    def run(self):
        self.display_menu()

    def display_menu(self):
        # (url, ListItem, IsDirectory?)
        categories = [
            ('', xbmcgui.ListItem('Films'), True),
            ('', xbmcgui.ListItem('Football'), True)
        ]
        xbmcplugin.setContent(self.proc_id, 'movies')
        # Last param for progressbar
        xbmcplugin.addDirectoryItems(self.proc_id, categories, len(categories))
        xbmcplugin.endOfDirectory(self.proc_id)

if __name__ == '__main__':
    app = App(sys.argv[0], sys.argv[1], sys.argv[2])
    app.run()