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
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton

kivy.require("2.1.0")
Window.size = consts.DEFAULT_WINDOW_SIZE


class MainRemoteScreen(MDScreen):
    """
    Main remote control interface.
    """

    def on_pre_enter(self):
        # update_all_buttons()
        self.main_top_section.power_state_section.update_power_state(
            self.remote.ROKU_POWER_STATE)

    def receive_remote(self, remote):
        self.remote = remote


class ControllerTopSection(MDRelativeLayout):
    """
    Top section of main controller GUI.
    """
    pass


class PowerState(Button):
    """
    Section containing Roku device/power-state info.
    """

    def update_power_state(self, power_state):
        self.text = f"POWER_STATE: {power_state}"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PowerButton(MDFillRoundFlatButton):
    """
    Power button widget on remote control GUI.
    """

    def power_button_press(self):
        ROOT_MAIN_SCR = MDApp.get_running_app().root.ids.main_remote_scr
        POWER_STATE_WIDGET = (
            MDApp.get_running_app().
            root.ids.main_remote_scr.
            ids.main_top_section.
            ids.power_state_section)
        ROOT_MAIN_SCR.remote.power_toggle()
        POWER_STATE = (
            MDApp.get_running_app().root.
            ids.main_remote_scr.remote.ROKU_POWER_STATE)
        POWER_STATE_WIDGET.update_power_state(POWER_STATE)


class RootScreenManager(MDScreenManager):
    """
    Main screen manager for RomotePyApp
    """

    def hand_remote(self, scr_name, remote):
        scr = self.get_screen(scr_name)
        scr.receive_remote(remote)

    def set_screen(self, scr_name, remote):
        self.hand_remote(scr_name, self.remote)
        self.current = scr_name

    def __init__(self, remote, *args, **kwargs):
        self.remote = remote
        super().__init__(*args, **kwargs)
        if self.remote.CONTACT_ESTABLISHED:
            self.set_screen(self.main_remote_scr.name, self.remote)
        else:
            self.set_screen(self.init_setup_scr.name, self.remote)


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
