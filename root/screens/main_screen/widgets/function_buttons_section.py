from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.relativelayout import MDRelativeLayout


class ControllerFunctionButtonsSection(MDRelativeLayout):
    """
    Section of the remote control that contains all functionality buttons.
    """
    pass


class FunctionButtons(MDIconButton):
    pass


class ReverseButton(FunctionButtons):
    """
    Reverse/rewind button class
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.reverse()


class ForwardButton(FunctionButtons):
    """
    Fast-forward button class
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.forward()


class BackButton(FunctionButtons):
    """
    Back button class
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.back()


class HomeButton(FunctionButtons):
    """
    Home button class
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.home()


class MuteButton(FunctionButtons):
    """
    Mute button class
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.volume_mute()


class VolUpButton(FunctionButtons):
    """
    Volume-up button class.
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.volume_up()


class SendTextButton(FunctionButtons):
    """
    Button to send a typed string to Roku devices.
    """
    pass


class PlayPauseButton(FunctionButtons):
    """
    Play/pause media button
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.play()


class VolDownButton(FunctionButtons):
    """
    Volume-down button class.
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.volume_down()


class InfoButton(FunctionButtons):
    """
    Info button (star-icon button on physical Roku remote) class
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.info()


class ChannelUpButton(FunctionButtons):
    """
    Channel up button
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.channel_up()


class ChannelDownButton(FunctionButtons):
    """
    Channel down button
    """

    def on_press(self):
        MDApp.get_running_app().root.current_screen.remote.channel_down()
