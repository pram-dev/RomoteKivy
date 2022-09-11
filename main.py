"""
GUI implementation of romote.py
"""

import kivy
import consts
from romote import Romote
from configparser import ConfigParser
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

kivy.require("2.1.0")


class RootScreenManager(MDScreenManager):
    """
    Main Screen Manager controlling all app screens
    """
    pass


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
        screen_manager = RootScreenManager()
        return screen_manager


if __name__ == "__main__":
    RomotePyApp().run()
