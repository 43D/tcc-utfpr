from src.core.DatabaseLocal.DatabaseCore import DatabaseCore
from src.core.Utils.GoogleUtils.GoogleCredentialsUtils import GoogleCredentialsUtils
from src.infra.API.GoogleApiV1 import GoogleApiV1

class GoogleACL:
    def __init__(self, db: DatabaseCore, google_api: GoogleApiV1, google_util: GoogleCredentialsUtils):
        self._db = db
        self._google_api = google_api
        self._google_util = google_util

    def new_account_login(self):
        # get new login
        # save new login in sqlite
        # return id account or account obj
        ...

    def auto_refresh_tokens(self, id_account: int) -> bool:
        # get login in db
        # refresh token
        # if not refresh, return boolean 
        ...

    def force_refresh_tokens(self, id_account: int) -> bool:
        # get login in db
        # refresh token in auto_refresh_tokens
        # if fail, force new_account_login and replace id
        # return id account or account obj
        ...


    def send_video_from_pc(self, video_path: str, id_account: int):
        # get tokens e save self._tokens
        # refresh tokens
        # if not refresh, raise custom exception
        # check file exists and is valid, if not, raise excepiton
        # send_api code
        ...

    def send_thumbnail_from_pc(self, id_account: int):
        ...