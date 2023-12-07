#!/usr/bin/env bash

export LOG_LEVEL=INFO
export WAIT_TIME=3600
export DISCORD_USERNAME="storage-bridge"
export DISCORD_TRIGGER=on
export REDIS_HOST="storage-bridge-redis"
export REDIS_PORT=6379
export REDIS_TTL=2678400
export STORAGE_BRIDGE_VERSION="${CI_COMMIT_BRANCH}-${CI_COMMIT_SHORT_SHA}"
export BUCKET_FOLDER="YYYY-MM"
