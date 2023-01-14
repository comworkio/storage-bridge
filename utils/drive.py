import os

from googleapiclient.discovery import build
from utils.common import is_disabled
from utils.logger import log_msg

API_KEY = os.getenv('GOOGLE_API_KEY')

drive_service = None
if not any(is_disabled(setting) for setting in [API_KEY]):
    drive_service = build('drive', 'v3', developerKey=API_KEY)

def get_drive_service():
    return drive_service
