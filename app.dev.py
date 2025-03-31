from src.Api import Api
from src.infra.database.DatabaseFactory import DatabaseFactory
from src.RunApp import RunApp

def start ():
    debug = True    
    db = DatabaseFactory()
    api = Api(db=db, debug=debug)
    RA = RunApp(api=api, debug=debug, debug_tool=debug)
    RA.run()

if __name__ == '__main__':
    start()