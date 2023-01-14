# storage-bridge

This project aim to be able to download documents from object storages such as S3 buckets and upload into Google drive.

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/storage-bridge
* Github mirror: https://github.com/idrissneumann/storage-bridge.git
* Gitlab mirror: https://gitlab.com/ineumann/storage-bridge.git

## Image on the dockerhub

The image is available and versioned here: https://hub.docker.com/r/comworkio/storage-bridge

You'll find tags for arm32/aarch64 (optimized for raspberrypi) and x86/amd64 tags.

## Getting started

```shell
$ cp .env.dist .env # replace the environment values in this file
$ docker-compose -f docker-compose-local.yml up --force-recreate
```

And if you want to change the python sources, don't forget to rebuild:

```shell
$ cp .env.dist .env # replace the environment values in this file
$ docker-compose -f docker-compose-local.yml up --force-recreate --build
```

For generating a Google drive API key:
* [Enable this API](https://console.cloud.google.com/flows/enableapi?apiid=drive.googleapis.com)
* [Go to credentials](https://console.cloud.google.com/apis/credentials)
* Click Create Credentials > Service Account

The result should be like:
![sa](./img/sa.png)

* Create a key and choose the JSON format and hash the content in base64
![json_key](./img/json_key.png)

* Copy-paste the base64 content in the `GOOGLE_SA_B64` environment variable

* Create a folder on drive and share-it with the service account:

![share](./img/share.png)

Copy-paste the folder id into the `GOOGLE_DRIVE_FOLDER_ID` environment variable

## Restful API

### Healthcheck

```shell
$ curl localhost:8080/v1/health
{"status": "ok", "alive": true}
```

### Manifests

```shell
$ curl localhost:8080/v1/manifest 
{"version": "1.0", "sha": "1c7cb1f", "arch": "x86"}
```
