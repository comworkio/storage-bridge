import os

from time import sleep
from utils.logger import log_msg

WAIT_TIME = int(os.environ['WAIT_TIME'])

def bridge():
    log_msg("INFO", "[storage-bridge] deployment of version {} !".format(os.environ['STORAGE_BRIDGE_VERSION']))
    sleep(WAIT_TIME)
