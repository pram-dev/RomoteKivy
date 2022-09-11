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
        test_command = Romote.safe_command_wrapper(self.up)
        success = test_command()
        if success:
            self.CONTACT_ESTABLISHED = True

    def __init__(self, host=None, *args, **kwargs):

        if host:
            super().__init__(host, *args, **kwargs)
            self.attempt_first_contact()

    def attempt_contact(ip_str):
        pass

    CONTACT_ESTABLISHED = False
