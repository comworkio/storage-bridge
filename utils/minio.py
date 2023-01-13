import os

from minio import Minio
from utils.common import is_disabled

BUCKET_URL = os.getenv('BUCKET_URL')
BUCKET_ACCESS_KEY = os.getenv('BUCKET_ACCESS_KEY')
BUCKET_SECRET_KEY = os.getenv('BUCKET_SECRET_KEY')

minioClient = None

if not any(is_disabled(setting) for setting in [BUCKET_URL, BUCKET_ACCESS_KEY, BUCKET_SECRET_KEY]):
    minioClient = Minio(os.environ['BUCKET_URL'],
                    access_key=os.environ['BUCKET_ACCESS_KEY'],
                    secret_key=os.environ['BUCKET_SECRET_KEY'],
                    secure=True)

def get_minio_client():
    return minioClient
