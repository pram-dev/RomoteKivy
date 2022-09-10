"""
GUI implementation of romote.py
"""

import kivy
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

kivy.require("2.1.0")


class RootScreenManager(MDScreenManager):
    """
    Main Screen Manager controlling all app screens
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