import os
import time
import webview
from src.controller.DatabaseLocal.DatabaseController import DatabaseController
from src.controller.EncryptData.EncryptDataController import EncryptDataController
from src.controller.Utils.UtilsController import UtilsController
from src.core.DatabaseLocal.DatabaseCore import DatabaseCore
from src.core.EncryptData.EncryptDataCore import EncryptDataCore
from src.core.Utils.DialogMenu import DialogMenu
from src.core.Utils.Timer import Timer
from src.core.Utils.WindowsUtils import WindowsUtils
from src.infra.database.DatabaseFactory import DatabaseFactory

class Api:
    def __init__(self, db: DatabaseFactory, debug: bool = False) -> None:
        self._db = db.create()
        self._init_encrypt_core()
        self._init_database()
        self._init_utilitarios()
      
    def _init_encrypt_core(self):
        module = EncryptDataCore()
        self._encrytpData = EncryptDataController(module=module)

    def _init_database(self):
        module = DatabaseCore(databse=self._db, encrytpData=self._encrytpData)
        self.databaseController = DatabaseController(module=module)

    def _init_utilitarios(self):
        windowsModule = WindowsUtils()
        timerModule = Timer()
        dialogMenu = DialogMenu()
        self.utils = UtilsController(dialogMenu=dialogMenu, timerModule=timerModule, windowsModule=windowsModule)
