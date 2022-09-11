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
            except (gaierror, ConnectTimeout, ConnectionError):
                print("Could not contact device.")
                success = False

            return success
        return safe_command_func

    def attempt_first_contact(self):
        success = self.up()
        if success:
            self.CONTACT_ESTABLISHED = True

    def __init__(self, host=None, *args, **kwargs):
        self.safe_wrap_all_commands(Romote.safe_command_wrapper)

        if host:
            super().__init__(host, *args, **kwargs)
            self.attempt_first_contact()

    def safe_wrap_all_commands(self, wrapper_func):

        self.up = wrapper_func(self.up)
        self.right = wrapper_func(self.right)
        self.down = wrapper_func(self.down)
        self.left = wrapper_func(self.left)
        self.select = wrapper_func(self.select)
        self.back = wrapper_func(self.back)

    CONTACT_ESTABLISHED = False
