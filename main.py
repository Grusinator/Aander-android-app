import os
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.properties import ObjectProperty, StringProperty
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


from adventures import AdventuresScreen, TreasuresScreen, LibraryScreen, CluesScreen, LoginScreen, SignUpScreen


class MainScreen(Screen):
    pass



class AanderApp(App):
    #presentation = Builder.load_file("aander.kv")
    #screen_manager = ObjectProperty(None)

    def search(self):
        pass


    def build(self):
        self.menu_height = 200


        #self.recognizer = Recognizer()

        # declare the ScreenManager as a class property
        self.screen_manager = ScreenManager(transition=FadeTransition(
                                     duration=.15))


        self.main_screen = MainScreen()
        main_screen = Screen(name = 'menu')
        main_screen.add_widget(self.main_screen)
        self.screen_manager.add_widget(main_screen)


        self.login_screen = LoginScreen()
        login_screen = Screen(name = 'login')
        login_screen.add_widget(self.login_screen)
        self.screen_manager.add_widget(login_screen)

        self.signup_screen = SignUpScreen()
        signup_screen = Screen(name = 'signup')
        signup_screen.add_widget(self.signup_screen)
        self.screen_manager.add_widget(signup_screen)


        self.adventure = AdventuresScreen()
        adventurescreen = Screen(name='adventures')
        adventurescreen.add_widget(self.adventure)
        self.screen_manager.add_widget(adventurescreen)

        self.treasures = TreasuresScreen()
        treasuresscreen = Screen(name='treasures')
        treasuresscreen.add_widget(self.treasures)
        self.screen_manager.add_widget(treasuresscreen)


        self.library = LibraryScreen()
        libraryscreen = Screen(name='library')
        libraryscreen.add_widget(self.library)
        self.screen_manager.add_widget(libraryscreen)

        self.clues = CluesScreen()
        cluesscreen = Screen(name='clues')
        cluesscreen.add_widget(self.clues)
        self.screen_manager.add_widget(cluesscreen)

        self.screen_manager.current = 'login'

        return self.screen_manager

if __name__ == "__main__":
    AanderApp().run()