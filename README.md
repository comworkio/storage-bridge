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
