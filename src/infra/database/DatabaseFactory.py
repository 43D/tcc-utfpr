from src.infra.database.Database import Database
from src.infra.database.DatabaseCreator import DatabaseCreator

class DatabaseFactory:
    def __init__(self):
        self._dbCreator: DatabaseCreator = None
        self._db: Database = None

    @staticmethod
    def _init_database(func):
        def wrapper(self, *args, **kwargs):
            if not self._dbCreator:
                self._dbCreator = DatabaseCreator()
            if not self._db:
                self._db = Database(factory=self._dbCreator)
            return func(self, *args, **kwargs)
        return wrapper
    
    @_init_database
    def create(self) -> Database:
        return self._db