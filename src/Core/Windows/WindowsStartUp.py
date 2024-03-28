import os
import win32com.client
from src.DB.DatabaseFactory import DatabaseFactory

class WindowsStartUp:
    def __init__(self, project_folder: str) -> None:
        self._project_folder = project_folder
        self._db = DatabaseFactory().create()
        self._check_start_up_windows()
        
    def _check_start_up_windows(self):
        res = self._db.getTagValue("WindowsStartUp")
        if res[1] == "1":
            self._create_shortcut()
        else:
            self._delete_shortcut()

    def _create_shortcut(self, wDir='', icon=''):
        desktop_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup') 
        path = os.path.join(desktop_path, 'SARC Cliente - Secretaria de Administração Rocha Contabilidade e Gestão.lnk')
        print(path)
        if not os.path.isfile(path):
            print("-create")
            
            target = os.path.join(self._project_folder, 'rocha.exe')
            shell = win32com.client.Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            if icon == '':
                shortcut.IconLocation = target
            else:
                shortcut.IconLocation = icon
            shortcut.save()
            
    def _delete_shortcut(self):
        desktop_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup') 
        path = os.path.join(desktop_path, 'SARC Cliente - Secretaria de Administração Rocha Contabilidade e Gestão.lnk')
        if os.path.isfile(path):
            os.remove(path)

