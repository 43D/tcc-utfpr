from src.core.Utils.DialogMenu import DialogMenu
from src.core.Utils.Timer import Timer
from src.core.Utils.WindowsUtils import WindowsUtils

class UtilsController:
    def __init__(
        self,
        windowsModule: WindowsUtils,
        timerModule: Timer,
        dialogMenu: DialogMenu
    ):
        self._windowsModule = windowsModule
        self._timerModule = timerModule
        self._dialogMenu = dialogMenu

    def save_file_dialog(self, type_file: str = "file", filename: str = "nome"):
        return self._dialogMenu.save_file_dialog(filename=filename, type_file=type_file)
    
    def open_folder_if_exists(self, path: str):
        return self._windowsModule.open_folder_if_exists(path=path)
    
    def check_file_exists(self, filepath: str):
        return self._windowsModule.check_file_exists(filepath=filepath)
            
    def sleep_timer(self, seconds: int):
        return self._timerModule.sleep_timer(seconds=seconds)
