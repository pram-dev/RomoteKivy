from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


class RootScreenManager(MDScreenManager):
    """
    Main screen manager for RomotePyApp
    """

    def set_screen(self, scr_name):
        self.current = scr_name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        remote = MDApp.get_running_app().controller
        if remote.CONTACT_ESTABLISHED:
            self.set_screen(self.main_remote_scr.name)
        else:
            self.set_screen(self.init_setup_scr.name)
