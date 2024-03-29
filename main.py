"""
GUI implementation of romote.py
"""

import kivy
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from utilities import consts
from utilities.romote import Romote
from configparser import ConfigParser
from root.romote_screen_mgr import RootScreenManager
from root.screens.main_screen.widgets.dpad_section import ControllerDPadSection
from root.screens.main_screen.main_remote_screen import MainRemoteScreen
from root.screens.main_screen.widgets.controller_top_section import (
    ControllerTopSection)
from root.screens.main_screen.widgets.function_buttons_section import (
    ControllerFunctionButtonsSection)


kivy.require("2.1.0")
Window.size = consts.DEFAULT_WINDOW_SIZE
Builder.load_file(consts.ROMOTE_PY_KV)


class RomotePy(MDApp):
    """
    Base Romote app
    """

    controller = None

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
    RomotePy().run()
