import os

from minio import Minio
from utils.common import is_disabled

BUCKET_URL = os.getenv('BUCKET_URL')
BUCKET_ACCESS_KEY = os.getenv('BUCKET_ACCESS_KEY')
BUCKET_SECRET_KEY = os.getenv('BUCKET_SECRET_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')
BUCKET_FOLDER = os.getenv('BUCKET_FOLDER')

minioClient = None

if not any(is_disabled(setting) for setting in [BUCKET_URL, BUCKET_ACCESS_KEY, BUCKET_SECRET_KEY, BUCKET_NAME, BUCKET_FOLDER]):
    minioClient = Minio(BUCKET_URL,
                    access_key=BUCKET_ACCESS_KEY,
                    secret_key=BUCKET_SECRET_KEY,
                    secure=True)

def get_minio_client():
    return minioClient

def get_bucket_name():
    return BUCKET_NAME

def get_bucket_folder():
    if is_disabled(BUCKET_FOLDER):
        return None

    return "{}/".format(BUCKET_FOLDER)
