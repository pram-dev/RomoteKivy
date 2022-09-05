"""
GUI implementation of romote.py
"""

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout

kivy.require("2.1.0")


class MainPage(GridLayout):
    """
    Main remote control page
    """

    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)


class AppsPage(GridLayout):
    pass


class SettingsPage(GridLayout):
    pass


class RemoteControl(PageLayout):
    """
    Main RemoteControl layout
    """

    def __init__(self, **kwargs):
        super(RemoteControl, self).__init__(**kwargs)


class RomoteApp(App):
    """
    Main RomoteApp
    """

    def build(self):
        control = RemoteControl()
        # control.contact_tv()
        return control


if __name__ == "__main__":
    RomoteApp().run()
