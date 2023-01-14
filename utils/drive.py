import os

from googleapiclient.discovery import build
from utils.common import is_disabled, is_empty
from utils.logger import log_msg

API_KEY = os.getenv('GOOGLE_API_KEY')
DRIVE_FOLDER = os.getenv('GOOGLE_DRIVE_FOLDER')

drive_service = None
if not any(is_disabled(setting) for setting in [API_KEY]):
    drive_service = build('drive', 'v3', developerKey=API_KEY)

def get_drive_service():
    return drive_service

def get_drive_folder():
    if is_empty(DRIVE_FOLDER):
        return ""
    return "{}/".format(DRIVE_FOLDER)
