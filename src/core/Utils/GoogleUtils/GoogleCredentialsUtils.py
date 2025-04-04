import json
from google.oauth2.credentials import Credentials

class GoogleCredentialsUtils:
    def converte_creds_to_json(self, creds: Credentials) -> dict[str, str]:
        return json.loads(creds.to_json())
    
    def converte_json_to_creds(self, creds_json: dict[str, str]) -> Credentials:
        return Credentials.from_authorized_user_info(creds_json, creds_json.get('scopes'))
