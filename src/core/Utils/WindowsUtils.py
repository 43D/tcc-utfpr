import os

class WindowsUtils:
    def open_folder_if_exists(self, path: str):
        if os.path.exists(path):
            os.startfile(path)

    def check_file_exists(self, filepath: str) -> bool:
        return os.path.isfile(path=filepath)