"""
GUI implementation of romote.py
"""

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

kivy.require("2.1.0")


class AppRootLayout(GridLayout):
    """
    Main Layout for main screen
    """
    pass


class RomoteApp(App):
    """
    Base Romote app
    """

    def build(self):
        return AppRootLayout()


if __name__ == "__main__":
    RomoteApp().run()