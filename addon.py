# coding: utf-8
import sys
import os
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import json


class Plugin:
    def __init__(self, base_url, proc_id, query):
        self.base_url = base_url
        self.proc_id = int(proc_id)
        self.query = query
        self.addon = xbmcaddon.Addon(id='plugin.video.darostream')
        # To be suitible with all OSs
        self.dir = xbmc.translatePath(self.addon.getAddonInfo('path'))
        self.images_dir = os.path.join(self.dir, 'resources', 'media')

    def run(self):
        if self.query == '':
            self.display_main_menu()
        else:
            q = self.parse_query()
            if q.get('setDirectory') == 'movies':
                self.display_movies_menu()
            elif q.get('setDirectory') == 'football':
                pass
            elif q.get('action') == 'searchMovie':
                self.search_movie(self.get_input())

    def display_main_menu(self):
        # Items to be displayed
        films = xbmcgui.ListItem('Films')
        films.setArt({
            'fanart': os.path.join(self.images_dir, 'fanart_films.jpg'),
            'icon': os.path.join(self.images_dir, 'icon_movies.png')
        })
        foot = xbmcgui.ListItem('Football')
        foot.setArt({
            'fanart': os.path.join(self.images_dir, 'fanart_foot.jpg'),
            'icon': os.path.join(self.images_dir, 'icon_foot.png')
        })
        # (url, ListItem, IsDirectory?)
        items = [
            (self.base_url+'?setDirectory=movies', films, True),
            (self.base_url+'?setDirectory=movies', foot, True),
        ]
        xbmcplugin.setContent(self.proc_id, 'movies')
        # Last param for progressbar
        xbmcplugin.addDirectoryItems(self.proc_id, items, len(items))
        xbmcplugin.endOfDirectory(self.proc_id)

    def display_movies_menu(self):
        # Items to be displayed
        search = xbmcgui.ListItem('Rechercher')
        search.setArt({
            'fanart': os.path.join(self.images_dir, 'fanart_films.jpg'),
            'icon': os.path.join(self.images_dir, 'icon_search.png')
        })
        # (url, ListItem, IsDirectory?)
        items = [
            (self.base_url+'?action=searchMovie', search, True),
        ]
        xbmcplugin.setContent(self.proc_id, 'movies')
        # Last param for progressbar
        xbmcplugin.addDirectoryItems(self.proc_id, items, len(items))
        xbmcplugin.endOfDirectory(self.proc_id)

    def search_movie(self):
        pass

    def get_input(self):
        kb = xbmc.Keyboard('', 'Entrez le nom du film')
        kb.doModal()
        if kb.isConfirmed():
            return kb.getText()
        else:
            return ''

    def parse_query(self):
        queries = {}
        # Parsing query of form ?a=1&b=2 in [a=1, b=2]
        tmp = self.query.replace('?', '').encode().split('&')
        for i in tmp:
            q = i.split('=')
            queries[q[0]] = q[1]
        return queries

if __name__ == '__main__':
    plugin = Plugin(sys.argv[0], sys.argv[1], sys.argv[2])
    plugin.run()