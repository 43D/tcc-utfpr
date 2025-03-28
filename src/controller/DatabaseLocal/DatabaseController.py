from src.core.DatabaseLocal.DatabaseCore import DatabaseCore

class DatabaseController:
    def __init__(self, module: DatabaseCore) -> None:
        self._module = module
    
    def get_attr(self, tag: str):
        return self._module.get_attr(tag)

    def update_attr(self, tag: str, value: str):
        return self._module.update_attr(tag, value)
