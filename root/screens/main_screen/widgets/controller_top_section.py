from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.uix.button import Button


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
