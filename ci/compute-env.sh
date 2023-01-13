#!/usr/bin/env bash

export LOG_LEVEL=INFO
export WAIT_TIME=60
export SLACK_CHANNEL="#storage-bridge"
export SLACK_EMOJI=":drive:"
export SLACK_USERNAME="storage-bridge"
export SLACK_TRIGGER=on
export STORAGE_BRIDGE_VERSION="${CI_COMMIT_BRANCH}-${CI_COMMIT_SHORT_SHA}"
