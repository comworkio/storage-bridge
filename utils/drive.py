import os

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from utils.common import is_disabled
from utils.logger import log_msg

CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
REDIRECT_SCHEME = os.getenv('GOOGLE_REDIRECT_SCHEME')
REDIRECT_HOST = os.getenv('GOOGLE_REDIRECT_HOST')
REDIRECT_PORT = os.getenv('GOOGLE_REDIRECT_PORT')
SCOPES = ['https://www.googleapis.com/auth/drive']

drive_service = None
if not any(is_disabled(setting) for setting in [CLIENT_ID, CLIENT_SECRET, REDIRECT_SCHEME, REDIRECT_HOST, REDIRECT_PORT]):
    redirect_uri = "{}://{}:{}".format(REDIRECT_SCHEME, REDIRECT_HOST, REDIRECT_PORT)
    log_msg("INFO", "Redirect uri is {}".format(redirect_uri))
    flow = InstalledAppFlow.from_client_config(
        client_config={
            "installed": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uris": [redirect_uri],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://accounts.google.com/o/oauth2/token"
            }
        },
        scopes=SCOPES
    )
    creds = flow.run_local_server(port=int(REDIRECT_PORT), host="0.0.0.0", open_browser=False)
    drive_service = build('drive', 'v3', credentials=creds)

def get_drive_service():
    return drive_service
