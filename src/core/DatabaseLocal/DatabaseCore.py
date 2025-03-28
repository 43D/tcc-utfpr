from src.infra.database.Database import Database
from src.controller.EncryptData.EncryptDataController import EncryptDataController

class DatabaseCore:
    def __init__(self, databse: Database, encrytpData: EncryptDataController) -> None:
        self._db = databse
        self._encrytpData = encrytpData

    def get_attr(self, tag: str):
        data: list[str] = self._db.getTagValue(tag=tag)
        return data[1]

    def update_attr(self, tag: str, value: str):
        self._db.updateTagValue(tag=tag, value=value)
        return self.get_attr(tag=tag)