"""
GUI implementation of romote.py
"""

import kivy
import consts
from romote import Romote
from configparser import ConfigParser
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.button import Button
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDFillRoundFlatButton

kivy.require("2.1.0")
Window.size = consts.DEFAULT_WINDOW_SIZE


class ControllerTopSection(MDRelativeLayout):
    """
    Top section of main controller GUI.
    """
    pass


class PowerState(Button):
    """
    Section containing Roku device/power-state info.
    """
    pass


class PowerButton(MDFillRoundFlatButton):
    """
    Power button widget on remote control GUI.
    """
    pass


class RootScreenManager(MDScreenManager):
    """
    Main screen manager for RomotePyApp
    """

    def __init__(self, remote, *args, **kwargs):
        self.remote = remote
        super().__init__(*args, **kwargs)
        if self.remote.CONTACT_ESTABLISHED:
            self.current = RootScreenManager.main_remote_scr.name
        else:
            self.current = RootScreenManager.init_setup_scr.name


class RomotePyApp(MDApp):
    """
    Base Romote app
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.controller = Romote()

        config = ConfigParser()
        config.read(consts.CACHE_FILE)

        if config.has_option(consts.SECTION_CACHED, consts.KEY_LAST_IP):
            cached_ip = config.get(consts.SECTION_CACHED, consts.KEY_LAST_IP)
            self.controller.attempt_first_contact(cached_ip)

    def build(self):
        screen_manager = RootScreenManager(self.controller)
        return screen_manager


if __name__ == "__main__":
    RomotePyApp().run()
