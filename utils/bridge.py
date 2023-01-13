import os

from time import sleep
from utils.logger import log_msg
from utils.minio import get_bucket_folder, get_bucket_name, get_minio_client

WAIT_TIME = int(os.environ['WAIT_TIME'])

def bridge():
    log_msg("INFO", "[storage-bridge] deployment of version {} !".format(os.environ['STORAGE_BRIDGE_VERSION']))
    minioClient = get_minio_client()
    files = minioClient.list_objects(get_bucket_name(), prefix=get_bucket_folder(), recursive=True)
    for file in files:
        log_msg("INFO", "[storage-bridge] processing file {}".format(file))
    sleep(WAIT_TIME)
