from src.infra.database.DatabaseCreator import DatabaseCreator

class Database:
    def __init__(self, factory: DatabaseCreator):
        self._conn = factory.getConn()

    def getTagValue(self, tag: str):
        try:
            res = ()
            cursor = self._conn.cursor()
            cursor.execute("SELECT `tag`, `value` FROM `config` WHERE `tag` = ? LIMIT 1;", (tag,))
            res =  cursor.fetchone()
        finally:
            cursor.close()
            return res
        
    def updateTagValue(self, tag: str, value: str):
        try:
            cursor = self._conn.cursor()
            cursor.execute('''
                UPDATE `config`
                SET value = ?
                WHERE tag = ?
            ''', (value, tag))
            self._conn.commit()
        finally:
            cursor.close()

    def __del__(self):
        self._conn.close()
