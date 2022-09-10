from roku import Roku


class Romote(Roku):
    """
    Wrapper for Roku class to better integrate with GUI
    """

    CONTACT_ESTABLISHED = False

    def __init__(self, host=None, *args, **kwargs):

        if host:
            super().__init__(host, *args, **kwargs)

    def attempt_contact(ip_str):
        pass
