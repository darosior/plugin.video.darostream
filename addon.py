# coding: utf-8
import sys
import os
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin


class Plugin:
    def __init__(self, base_url, proc_id, query=''):
        self.base_url = str(base_url)
        self.proc_id = int(proc_id)
        self.query = query
        self.addon = xbmcaddon.Addon(id='plugin.video.darostream')
        self.dir = xbmc.translatePath(self.addon.getAddonInfo('path'))
        self.images_dir = os.path.join(self.dir, 'resources', 'media')

    def run(self):
        self.display_menu()

    def display_menu(self):
        # Main menu
        # Items to be displayed
        films = xbmcgui.ListItem('Films')
        films.setArt({
            'fanart': os.path.join(self.images_dir, 'fanart_films.jpg'),
            'icon': os.path.join(self.images_dir, 'icon_films.png')
        })
        foot = xbmcgui.ListItem('Football')
        foot.setArt({
            'fanart': os.path.join(self.images_dir, 'fanart_foot.jpg'),
            'icon': os.path.join(self.images_dir, 'icon_foot.png')
        })
        # (url, ListItem, IsDirectory?)
        items = [
            ('', films, True),
            ('', foot, True),
        ]
        xbmcplugin.setContent(self.proc_id, 'movies')
        # Last param for progressbar
        xbmcplugin.addDirectoryItems(self.proc_id, items, len(items))
        xbmcplugin.endOfDirectory(self.proc_id)

if __name__ == '__main__':
    plugin = Plugin(sys.argv[0], sys.argv[1], sys.argv[2])
    plugin.run()