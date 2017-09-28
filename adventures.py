import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.utils import platform
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.multistroke import Recognizer
from kivy.properties import ObjectProperty, StringProperty, NumericProperty

import httplib
import json




# class AdventureManager():
#     screen = None
#     adventures = []

    # def __init__(self):
    #     self.screen = self.AdventuresScreen()



# layout = GridLayout(cols=1, orientation='vertical', size_hint_y=None)
#
# layout.bind(minimum_height=layout.setter('height'))
#
# for row in range(24):
#     col1 = TextInput()
#     col2 = TextInput()
#     col3 = TextInput()
#     col4 = TextInput()
#     col5 = TextInput()
#     col6 = TextInput()
#     col7 = TextInput()
#     col8 = TextInput()
#     cols = [col1, col2, col3, col4, col5, col6, col7, col8]
#     row_layout = BoxLayout(orientation='horizontal', width=800, height=40, size_hint=(None, None))
#
#     for col in cols:
#         row_layout.add_widget(col)
#
#     layout.add_widget(row_layout)
#
# root = ScrollView(do_scroll_x=False)
# root.add_widget(layout)
# self.add_widget(root)








class AdventuresScreen(Screen):
    adventures_list = None
    def __init__(self):
        super(AdventuresScreen, self).__init__()

        self.updateadventurelist()


    def updateadventurelist(self):
        self.ids.adventures_list.clear_widgets()

        adventures_list = self.get_adventures_from_api()

        for adventure in adventures_list:
            adventure_widget = AdventureVisualizer(adventure)
            self.ids.adventures_list.add_widget(adventure_widget)

    def show_clues(self):
        pass


    def get_adventures_from_api(self):
        import httplib2 as http
        import json

        try:
            from urlparse import urlparse
        except ImportError:
            from urllib.parse import urlparse

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8'
        }

        uri = 'http://localhost:8000'
        path = '/myadventures/'

        target = urlparse(uri + path)
        method = 'GET'
        body = ''

        h = http.Http()

        # If you need authentication some example:
        # if auth:
        #    h.add_credentials(auth.user, auth.password)

        response, content = h.request(
            target.geturl(),
            method,
            body,
            headers)

        # assume that content is a json reply
        # parse content with the json module
        data = json.loads(content)

        return [Adventure(x['title'],x['description']) for x in data]



class Adventure():
    title = None
    description = None
    clues = []

    def __init__(self, title, description, clues = list()):
        self.title = title
        self.description = description
        self.clues = clues

class AdventureVisualizer(BoxLayout):
    title = StringProperty()
    description = StringProperty()

    def __init__(self, adventure):
        super(AdventureVisualizer, self).__init__()
        self.title = adventure.title
        self.description = adventure.description


class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    _username = ObjectProperty(None)
    _password = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(SignUpScreen, self).__init__(**kwargs)

    def createUserAccount(self):


        try:
            print "test1"
            connection = httplib.HTTPSConnection('127.0.0.1:8000', 443)
            connection.connect()

            print self._username

            body = json.dumps({
                "username": self._username,
                "password": self._password,
            })

            body = json.dumps({
                "username": "grusinator",
                "password": "test1234",
            })

            body2 = {
               #"X-Parse-Application-Id": "nfgytgRuqQwkOqHxEhOEHKisT4sAxFIbCoOvbR5q",
               #"X-Parse-REST-API-Key": "j9Qm7b6TuKZFiIAbONytGSWDLAAvWaie0dokk5nE",
               "Content-Type": "application/json"
           }

            print body2

            connection.request('POST', '/rest-auth/login/', body=body, headers=body2 )
            result = json.loads(connection.getresponse().read())
            print "test"
            print result
        except:
            print "Error: Unable to connect!"

#other -- should be moved later

class CluesScreen(Screen):
    clues = []

    def __init__(self):
        super(CluesScreen, self).__init__()

        # change to read from db later
        clues_list = [  Clue("title1"),
                        Clue("title1")]
        for clue in clues_list:
            clue_widget = CluesVisualizer(clue)
            self.ids.clues_list.add_widget(clue_widget)

class CluesVisualizer(BoxLayout):
    text = StringProperty()

    def __init__(self, clue):
        super(CluesVisualizer, self).__init__()
        self.text = clue.text



"""    Button:
    canvas:
        Color:
            rgba: 1, 1, 1, .5
        Rectangle:
            pos: self.pos
            size: self.siz
        on_release: app.root.current = 'clues'
        StackLayout:
            pos: self.parent.pos
            size: self.parent.size
            orientation: 'lr-tb'
            Image:
                source: 'images/map.jpg'
                size_hint_x: None
                width: 74
            Label:
                size_hint_x: None
                width: 100
                text: self.parent.parent.parent.title
            Label:
                size_hint_x: None
                width: 100
                text: self.parent.parent.parent.description"""


class Clue():
    text = None
    adventureid = None

    def __init__(self, text, adventureid = 0):
        self.text = text
        self.adventureid = adventureid




class SpellcastScreen(Screen):
    pass

class TreasuresScreen(Screen):
    pass

class LibraryScreen(Screen):
    pass