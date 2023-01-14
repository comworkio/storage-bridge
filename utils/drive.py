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
DRIVE_FOLDER = os.getenv('GOOGLE_DRIVE_FOLDER')

drive_service = None
if not any(is_disabled(setting) for setting in [SA_B64]):
    sa = base64.b64decode(SA_B64).decode('utf-8')
    creds = Credentials.from_service_account_info(json.loads(sa))
    drive_service = build('drive', 'v3', credentials=creds)

def get_drive_service():
    return drive_service

def get_drive_folder():
    if is_empty(DRIVE_FOLDER):
        return ""
    return "{}/".format(DRIVE_FOLDER)

def get_file_id(path):
    try:
        return drive_service.files().get(fileId=path, fields='id').execute()
    except HttpError as e:
        log_msg("DEBUG", "[drive][is_file_exists] the path {} not exists : {}".format(path, e))

def is_file_exists(path):
    return is_not_empty(get_file_id(path))

def create_folder(path):
    folder_metadata = {
        'name': path,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    try:
        return drive_service.files().create(body=folder_metadata, fields='id').execute()
    except HttpError as e:
        log_msg("ERROR", "[drive][create_folder] could not create folder {} : {}".format(path, e))
        return None

def upload_file(filename, path, mimetype):
    file_metadata = {
        'name': filename
    }
    
    filepath = "{}{}".format(path, filename)
    media = MediaFileUpload(filepath, mimetype=mimetype)
    try:
        return drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    except HttpError as e:
        log_msg("ERROR", "[drive][upload_file] could not file folder {} : {}".format(filepath, e))
        return None
