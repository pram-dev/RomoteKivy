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
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.button import MDIconButton

kivy.require("2.1.0")
Window.size = consts.DEFAULT_WINDOW_SIZE


class FunctionButtons(MDIconButton):
    pass


class BackButton(FunctionButtons):
    pass


class HomeButton(FunctionButtons):
    pass


class VolUpButton(FunctionButtons):
    pass


class VolDownButton(FunctionButtons):
    """
    Volume-down button class.
    """


class InfoButton(FunctionButtons):
    pass


class MainRemoteScreen(MDScreen):
    """
    Main remote control interface.
    """

    def on_pre_enter(self):
        # update_all_buttons()
        self.remote = MDApp.get_running_app().controller
        self.main_top_section.power_state_section.update_power_state(
            self.remote.ROKU_POWER_STATE)


class ControllerTopSection(MDRelativeLayout):
    """
    Top section of main controller GUI.
    """
    pass


class ControllerFunctionButtonsSection(MDRelativeLayout):
    """
    Section of the remote control that contains all functionality buttons.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PowerState(Button):
    """
    Section containing Roku device/power-state info.
    """

    def update_power_state(self, power_state):
        self.text = f"POWER_STATE: {power_state}"


class PowerButton(MDFillRoundFlatIconButton):
    """
    Power button widget on remote control GUI.
    """

    def on_parent(self, power_button, parent):
        self.remote = MDApp.get_running_app().controller
        self.update_bg_color()

    def update_bg_color(self):
        power_state = self.remote.ROKU_POWER_STATE

        if power_state == "On":
            self.md_bg_color = (50 / 255, 188 / 255, 252 / 255, 0.8)
        elif power_state == "Off":
            self.md_bg_color = (223 / 255, 70 / 255, 97 / 255, 0.8)

    def power_button_press(self):
        self.remote.power_toggle()
        POWER_STATE_WIDGET = self.parent.ids.power_state_section
        POWER_STATE_WIDGET.update_power_state(self.remote.ROKU_POWER_STATE)
        self.update_bg_color()


class RootScreenManager(MDScreenManager):
    """
    Main screen manager for RomotePyApp
    """

    def set_screen(self, scr_name):
        self.current = scr_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        remote = MDApp.get_running_app().controller
        if remote.CONTACT_ESTABLISHED:
            self.set_screen(self.main_remote_scr.name)
        else:
            self.set_screen(self.init_setup_scr.name)


class RomotePyApp(MDApp):
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
    RomotePyApp().run()
