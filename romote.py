from roku import Roku
from socket import gaierror
from requests.exceptions import ConnectTimeout, ConnectionError


class Romote(Roku):
    """
    Wrapper for Roku class to better integrate with GUI.
    Also, adds wrappers for Roku commands to make them safer by
    handling exceptions when contact with host fails.
    """

    @staticmethod
    def safe_command_wrapper(command_func):
        def safe_command_func(*arg):
            try:
                if arg:
                    command_func(arg)
                elif not arg:
                    command_func()
                success = True
                print("success asdflsajdfaskldfjsafuh")
            except (gaierror, ConnectTimeout, ConnectionError):
                print("Could not contact device.")
                success = False

            return success
        return safe_command_func

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
        # method to safely retrieve apps list
        # method to safely launch app

    def attempt_first_contact(self):
        success = self.up()
        if success:
            self.CONTACT_ESTABLISHED = True

    def __init__(self, host=None, *args, **kwargs):
        self.safe_wrap_all_commands()

        if host:
            super().__init__(host, *args, **kwargs)
            self.attempt_first_contact()

    CONTACT_ESTABLISHED = False
