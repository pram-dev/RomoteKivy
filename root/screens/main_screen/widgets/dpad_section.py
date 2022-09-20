from os.path import join
from kivymd.uix.widget import MDWidget
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.graphics.svg import Svg


class DPadSVG(MDWidget):

    def __init__(self, filename=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        filename = join("svg", "dpad.svg")
        with self.canvas:
            self.svg = Svg(filename)
        self.size = self.svg.width, self.svg.height


class ControllerDPadSection(MDRelativeLayout):
    pass
