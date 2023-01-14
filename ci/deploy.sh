#!/usr/bin/env bash

source ./ci/compute-env.sh

ENV_FILE="storage_bridge.env"

echo "" > ${ENV_FILE}
echo "LOG_LEVEL=${LOG_LEVEL}" >> ${ENV_FILE}
echo "WAIT_TIME=${WAIT_TIME}" >> ${ENV_FILE}
echo "STORAGE_BRIDGE_VERSION=${STORAGE_BRIDGE_VERSION}" >> ${ENV_FILE}

env|grep -E "^(GOOGLE_|SLACK_|BUCKET_|REDIS_)"|while read -r; do
  echo "${REPLY}" >> "${ENV_FILE}"
done

docker rmi -f "comworkio/storage-bridge:${STORAGE_BRIDGE_VERSION}" || :
docker-compose -f docker-compose-intra.yml up -d --force-recreate
