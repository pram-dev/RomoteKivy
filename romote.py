from roku import Roku
from socket import gaierror
from requests.exceptions import ConnectTimeout, ConnectionError


class Romote(Roku):
    """
    Wrapper for Roku class to better integrate with a GUI.
    Also adds wrappers for Roku commands to make them safer by
    handling exceptions when contact with host fails.
    """

    @staticmethod
    def safe_command_wrapper(command_func):
        def safe_command_func(*args):
            try:
                if args:
                    command_func(args)
                elif not args:
                    command_func()
                success = True
            except (gaierror, ConnectTimeout, ConnectionError):
                print("Could not contact device.")
                success = False

            return success
        return safe_command_func

    def launch_app(self, app_index):
        app = self[app_index]
        if app:
            app.launch()
        else:
            print("App does not exist on current Roku device.")
        return

    def safe_wrap_all_commands(self, wrapper_func=safe_command_wrapper):

        self.input_hdmi1 = wrapper_func(self.input_hdmi1)
        self.input_hdmi2 = wrapper_func(self.input_hdmi2)
        self.input_hdmi3 = wrapper_func(self.input_hdmi3)
        self.input_hdmi4 = wrapper_func(self.input_hdmi4)
        self.input_tuner = wrapper_func(self.input_tuner)
        self.input_av1 = wrapper_func(self.input_av1)
        self.poweron = wrapper_func(self.poweron)
        self.poweroff = wrapper_func(self.poweroff)
        self.up = wrapper_func(self.up)
        self.right = wrapper_func(self.right)
        self.down = wrapper_func(self.down)
        self.left = wrapper_func(self.left)
        self.select = wrapper_func(self.select)
        self.back = wrapper_func(self.back)
        self.home = wrapper_func(self.home)
        self.info = wrapper_func(self.info)
        self.forward = wrapper_func(self.forward)
        self.reverse = wrapper_func(self.reverse)
        self.play = wrapper_func(self.play)
        self.replay = wrapper_func(self.replay)
        self.channel_up = wrapper_func(self.channel_up)
        self.channel_down = wrapper_func(self.channel_down)
        self.volume_up = wrapper_func(self.volume_up)
        self.volume_down = wrapper_func(self.volume_down)
        self.volume_mute = wrapper_func(self.volume_mute)
        self.search = wrapper_func(self.search)
        self.literal = wrapper_func(self.literal)
        self.launch_app = wrapper_func(self.launch_app)

    def attempt_first_contact(self, ip_str=None):
        if ip_str and not self.CONTACT_ESTABLISHED:
            super().__init__(ip_str)

        success = self.up()
        if success:
            self.CONTACT_ESTABLISHED = True
        else:
            self.CONTACT_ESTABLISHED = False

    def __init__(self, host=None, *args, **kwargs):
        self.safe_wrap_all_commands()

        if host:
            super().__init__(host, *args, **kwargs)
            self.attempt_first_contact()

    CONTACT_ESTABLISHED = False
    APP_LAUNCH_SUCCESS = False
