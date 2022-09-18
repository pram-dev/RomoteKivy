from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from root.screens.main_screen.widgets.controller_top_section import (
    ControllerTopSection)
from root.screens.main_screen.widgets.function_buttons_section import (
    ControllerFunctionButtonsSection)


class MainRemoteScreen(MDScreen):
    """
    Main remote control interface.
    """

    def on_pre_enter(self):
        # update_all_buttons()
        self.remote = MDApp.get_running_app().controller
        self.main_top_section.power_state_section.update_power_state(
            self.remote.ROKU_POWER_STATE)
