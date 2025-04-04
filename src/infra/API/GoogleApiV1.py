from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

class GoogleApiV1:
    def __init__(self, ):
        self._scopes = ['https://www.googleapis.com/auth/youtube.upload']
        self._secrets = r"E:\tcc-utfpr-2024-app\secrets\client_secret_225522396858-09j9bmsfp1a7lippfpj4idp9kvoq6fs7.apps.googleusercontent.com.json"

    def first_login_account(self) -> Credentials:
        flow = InstalledAppFlow.from_client_secrets_file(self._secrets, self._scopes)
        creds: Credentials = flow.run_local_server(port=8080)
        # creds_json = json.loads(creds.to_json())
        return creds
    
    def refresh_tokens(self, creds: Credentials) -> Credentials:
        ...

    def send_video_to_youtube(self, creds: Credentials, video_path: str) -> dict:
        ...
    