from os.path import join
from utilities.svg_widget import SvgWidget
from kivymd.uix.anchorlayout import MDAnchorLayout


class DPadSVG(SvgWidget):

    def __init__(self, filename, *args, **kwargs):
        super().__init__(filename, *args, **kwargs)


class ControllerDPadSection(MDAnchorLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        dpad_svg = join("svg", "dpad.svg")
        dpad = DPadSVG(dpad_svg)
        self.add_widget(dpad)
