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

        
    def updateGoogleCreds(self, creds_json: dict[str, str]) -> int | None:
        last_id = None
        try:
            cursor = self._conn.cursor()
            cursor.execute('''
            INSERT INTO google_tokens (token, refresh_token, token_uri, client_id, client_secret, scopes, expiry)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                creds_json.get('token'),
                creds_json.get('refresh_token'),
                creds_json.get('token_uri'),
                creds_json.get('client_id'),
                creds_json.get('client_secret'),
                ','.join(creds_json.get('scopes', [])),  # Scopes como string
                creds_json.get('expiry')
            ))
            last_id = cursor.lastrowid
            self._conn.commit()
        finally:
            cursor.close()
            return last_id
        
    def getGoogleCreds(self, id: int) -> tuple | None:
        try:
            res = ()
            cursor = self._conn.cursor()
            cursor.execute("SELECT * FROM google_tokens WHERE id = ?", (id,))
            res = cursor.fetchone()
        finally:
            cursor.close()
            return res

    def __del__(self):
        self._conn.close()
