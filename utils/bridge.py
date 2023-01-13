import os

from time import sleep
from utils.common import is_not_empty
from utils.logger import log_msg
from utils.minio import get_bucket_folder, get_bucket_name, get_minio_client

WAIT_TIME = int(os.environ['WAIT_TIME'])

def bridge():
    log_msg("INFO", "[storage-bridge] deployment of version {} !".format(os.environ['STORAGE_BRIDGE_VERSION']))
    minioClient = get_minio_client()
    if None == minioClient:
        log_msg("WARN", "[storage-bridge] unable to connect to the bucket... check the environment variables")
        return

    bucket_name = get_bucket_name()
    if not minioClient.bucket_exists(bucket_name):
        log_msg("WARN", "[storage-bridge] the bucket {} doesn't exists".format(bucket_name))
        return

    while True:
        bucket_folder = get_bucket_folder()
        
        log_msg("INFO", "[storage-bridge] listing bucket content : bucket = {}, folder = {}".format(bucket_name, bucket_folder))
        files = minioClient.list_objects(bucket_name, prefix=bucket_folder, recursive=True)
        for file in files:
            log_msg("INFO", "[storage-bridge] processing file {}".format(file))
        sleep(WAIT_TIME)
