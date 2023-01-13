import os
import requests

from utils.common import is_not_empty, is_true

LOG_LEVEL = os.environ['LOG_LEVEL']
SLACK_TRIGGER = os.environ['SLACK_TRIGGER']

def slack_message( message , is_public):
    if is_true(SLACK_TRIGGER):
        token = os.getenv('SLACK_TOKEN')
        if is_public and is_not_empty(os.getenv('SLACK_TOKEN_PUBLIC')):
            if is_not_empty(token):
                slack_message(message, False)
            token = os.environ['SLACK_TOKEN_PUBLIC']

        data = {"text": message, "username": os.environ['SLACK_USERNAME'], "channel": os.environ['SLACK_CHANNEL'], "icon_emoji": os.environ['SLACK_EMOJI'] }
        requests.post("https://hooks.slack.com/services/{}".format(token),json=data)

def discord_message( message , is_public):
    if is_true(SLACK_TRIGGER):
        token = os.getenv('DISCORD_TOKEN')
        if is_public and is_not_empty(os.getenv('DISCORD_TOKEN_PUBLIC')):
            if is_not_empty(token):
                discord_message(message, False)
            token = os.environ['DISCORD_TOKEN_PUBLIC']

        data = {"text": message, "username": os.environ['SLACK_USERNAME'] }
        requests.post("https://discord.com/api/webhooks/{}/slack".format(token),json=data)

def check_log_level ( log_level ):
    if LOG_LEVEL == "debug" or LOG_LEVEL == "DEBUG":
        return True
    else:
        return log_level != "debug" and log_level != "DEBUG"

def quiet_log_msg ( log_level, message ):
    if check_log_level(log_level):
        print ("[{}] {}".format(log_level, message))

def log_msg( log_level, message, is_public = False):
    if check_log_level(log_level):
        quiet_log_msg (log_level, message)
        slack_message(message, is_public)
        discord_message(message, is_public)
