import os
import sqlite3

class DatabaseCreator:
    def __init__(self) -> None:
        db_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'TCC') 
        if not os.path.exists(db_dir):
            os.makedirs(db_dir, exist_ok=True)
        db_path = os.path.abspath(os.path.join(db_dir, 'database.db'))
        self._conn = sqlite3.connect(db_path, check_same_thread=False)
        self._tabels_array()
        self._create_table_if_not_exists()
        self._insert_config_if_not_exists()
        
    def getConn(self):
        return self._conn

    def _tabels_array(self):
        self._tables = [
            """create table IF NOT EXISTS `config` (
                `tag` varchar(255) not null,
                `value` varchar(255) not null,
                UNIQUE(tag)
            )""",
            """CREATE TABLE IF NOT EXISTS google_tokens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token TEXT,
                refresh_token TEXT,
                token_uri TEXT,
                client_id TEXT,
                client_secret TEXT,
                scopes TEXT,
                expiry TEXT
            )"""
        ]
        
        self._tagsConfigs = [
            ["AppPath", "",],
            ["AppName", "TCC",],
        ]

    def _insert_config_if_not_exists(self):
        try:
            cursor = self._conn.cursor()
            for valor in self._tagsConfigs:
                cursor.execute('''
                    INSERT OR IGNORE INTO config (tag, value)
                    VALUES (?, ?)
                ''', (valor[0], valor[1]))
            self._conn.commit()
        finally:
            cursor.close()

    def _create_table_if_not_exists(self):
        try:
            cursor = self._conn.cursor()
            for valor in self._tables:
                cursor.execute(valor)
            self._conn.commit()
        finally:
            cursor.close()
