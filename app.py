import os
from src.Api import Api
from src.infra.database.DatabaseFactory import DatabaseFactory
from src.RunApp import RunApp

def start ():
    path = os.getcwd()
    index = os.path.join(path, 'view', 'index.html')
    db = DatabaseFactory()
    api = Api(db=db)
    RA = RunApp(url=index, api=api)
    RA.run()

if __name__ == '__main__':
    start()