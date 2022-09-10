"""
GUI implementation of romote.py
"""

import kivy
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

kivy.require("2.1.0")


class SettingsAboutScreen(MDScreen):
    """
    Screen containing settings and 'about' section
    """
    pass


class MainRemoteScreen(MDScreen):
    """
    Main/default screen containing remote
    """
    pass


class RootScreenManager(MDScreenManager):
    """
    Main Layout for main screen
    """
    pass


class RomoteApp(MDApp):
    """
    Base Romote app
    """

    def build(self):
        return RootScreenManager()


if __name__ == "__main__":
    RomoteApp().run()