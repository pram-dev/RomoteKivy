from utilities.svg_widget import SvgWidget
from kivymd.uix.anchorlayout import MDAnchorLayout


class ControllerDPadSection(MDAnchorLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        dpad = SvgWidget("svg/dpad.svg")
        dpad.scale = 1.5
        self.add_widget(dpad)