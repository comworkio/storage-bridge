import base64
import json
import os

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from utils.common import is_disabled, is_empty, is_not_empty
from utils.logger import log_msg

SA_B64 = os.getenv('GOOGLE_SA_B64')
DRIVE_FOLDER_ID = os.getenv('GOOGLE_DRIVE_FOLDER_ID')

drive_service = None
if not any(is_disabled(setting) for setting in [SA_B64, DRIVE_FOLDER_ID]):
    sa = base64.b64decode(SA_B64).decode('utf-8')
    creds = Credentials.from_service_account_info(json.loads(sa))
    drive_service = build('drive', 'v3', credentials=creds)

def get_drive_service():
    return drive_service

def get_drive_folder():
    return DRIVE_FOLDER_ID

def upload_file(filename, path, mimetype):
    file_metadata = {
        'name': filename,
        'parents': [get_drive_folder()]
    }
    filepath = "{}{}".format(path, filename)
    media = MediaFileUpload(filepath, mimetype=mimetype)
    try:
        return drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    except HttpError as e:
        log_msg("ERROR", "[drive][upload_file] could not file folder {} : {}".format(filepath, e))
        return None
