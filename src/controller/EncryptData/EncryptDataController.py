from src.core.EncryptData.EncryptDataCore import EncryptDataCore

class EncryptDataController:
    def __init__(self, module: EncryptDataCore):
        self._module = module

    def get_decode(self, string: str) -> str:
        return self._module.get_decode(string=string)
    
    def get_encode(self, string: str) -> str:
        return self._module.get_encode(string=string)