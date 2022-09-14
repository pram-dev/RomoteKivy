from roku import Roku
from socket import gaierror
from requests.exceptions import ConnectTimeout, ConnectionError


class Romote(Roku):
    """
    Wrapper for Roku class to better integrate with a GUI.
    Also adds wrappers for Roku commands to make them safer by
    handling exceptions when contact with host fails.
    """

    def _safe_command_wrapper(self, command_func):
        def safe_command_func(*args):
            try:
                if args:
                    command_func(*args)
                elif not args:
                    command_func()
                self.COMMAND_SUCCESSFUL = True
            except (gaierror, ConnectTimeout, ConnectionError):
                print("Could not contact device.")
                self.COMMAND_SUCCESSFUL = False
        return safe_command_func

    def launch_app(self, app_index):
        app = self[app_index]
        if app:
            app.launch()
            self.APP_LAUNCH_SUCCESSFUL = True
        else:
            print("App does not exist on current Roku device.")
            self.APP_LAUNCH_SUCCESSFUL = False

    def safe_wrap_all_commands(self, wrapper_func=_safe_command_wrapper):

        self.input_hdmi1 = wrapper_func(self, self.input_hdmi1)
        self.input_hdmi2 = wrapper_func(self, self.input_hdmi2)
        self.input_hdmi3 = wrapper_func(self, self.input_hdmi3)
        self.input_hdmi4 = wrapper_func(self, self.input_hdmi4)
        self.input_tuner = wrapper_func(self, self.input_tuner)
        self.input_av1 = wrapper_func(self, self.input_av1)
        self.poweron = wrapper_func(self, self.poweron)
        self.poweroff = wrapper_func(self, self.poweroff)
        self.up = wrapper_func(self, self.up)
        self.right = wrapper_func(self, self.right)
        self.down = wrapper_func(self, self.down)
        self.left = wrapper_func(self, self.left)
        self.select = wrapper_func(self, self.select)
        self.back = wrapper_func(self, self.back)
        self.home = wrapper_func(self, self.home)
        self.info = wrapper_func(self, self.info)
        self.forward = wrapper_func(self, self.forward)
        self.reverse = wrapper_func(self, self.reverse)
        self.play = wrapper_func(self, self.play)
        self.replay = wrapper_func(self, self.replay)
        self.channel_up = wrapper_func(self, self.channel_up)
        self.channel_down = wrapper_func(self, self.channel_down)
        self.volume_up = wrapper_func(self, self.volume_up)
        self.volume_down = wrapper_func(self, self.volume_down)
        self.volume_mute = wrapper_func(self, self.volume_mute)
        self.search = wrapper_func(self, self.search)
        self.literal = wrapper_func(self, self.literal)
        self.launch_app = wrapper_func(self, self.launch_app)

    def attempt_first_contact(self, ip_str=None):
        if ip_str and not self.CONTACT_ESTABLISHED:
            super().__init__(ip_str)

        try:
            self.ROKU_POWER_STATE = self.power_state
            self.CONTACT_ESTABLISHED = True
            print("Contact established!")
        except OSError:
            print("Could not establish contact.")
            self.CONTACT_ESTABLISHED = False

        # this up command is only being used during development to visually
        # indicate if Roku device has succesfully been contacted and has
        # received/executed the "up" command
        self.up()
        # self.up() only to visually indicate on Roku devices that contact
        # has been established

    def __init__(self, host=None, *args, **kwargs):
        self.CONTACT_ESTABLISHED = False
        self.COMMAND_SUCCESSFUL = False
        self.APP_LAUNCH_SUCCESSFUL = False
        self.ROKU_POWER_STATE = None

        self.safe_wrap_all_commands()

        if host:
            super().__init__(host, *args, **kwargs)
            self.attempt_first_contact()
