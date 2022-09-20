from os.path import join
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.scatter import Scatter
from kivy.graphics.svg import Svg


class DPadButton(Scatter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        filename = join("svg", "dpad.svg")
        with self.canvas:
            self.anchor_x = "center"
            self.anchor_y = "center"
            self.svg = Svg(filename)
            self.scale = 1.5
        self.size = self.svg.width, self.svg.height


class ControllerDPadSection(MDRelativeLayout):
    pass
