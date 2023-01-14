import os

from time import sleep
from utils.drive import get_drive_service, upload_file
from utils.logger import log_msg
from utils.minio import get_bucket_folder, get_bucket_name, get_bucket_tmp_dir, get_minio_client

WAIT_TIME = int(os.environ['WAIT_TIME'])

def bridge():
    log_msg("INFO", "[storage-bridge] deployment of version {} !".format(os.environ['STORAGE_BRIDGE_VERSION']))
    minioClient = get_minio_client()
    drive_service = get_drive_service()
    if None == minioClient:
        log_msg("WARN", "[storage-bridge] unable to connect to the bucket... check the environment variables")
        return

    if None == drive_service:
        log_msg("WARN", "[storage-bridge] unable to connect to google drive... check the environment variables")
        return

    bucket_name = get_bucket_name()
    tmp_dir = "{}/".format(get_bucket_tmp_dir())
    if not minioClient.bucket_exists(bucket_name):
        log_msg("WARN", "[storage-bridge] the bucket {} doesn't exists".format(bucket_name))
        return

    while True:
        bucket_folder = get_bucket_folder()
        
        log_msg("INFO", "[storage-bridge] listing bucket content : bucket = {}, folder = {}".format(bucket_name, bucket_folder))
        files = minioClient.list_objects(bucket_name, prefix=bucket_folder, recursive=True)
        for file in files:
            filepath = file.object_name
            filename = os.path.basename(filepath)
            log_msg("INFO", "[storage-bridge] processing file {}".format(filepath))
            minioClient.fget_object(bucket_name, filepath, tmp_dir + filename)
            upload_file(filename, tmp_dir, 'application/pdf')
            os.remove(tmp_dir + filename)
        sleep(WAIT_TIME)
