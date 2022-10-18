#!/usr/bin/bash

CURRENT=$(viewo --version)
RELEASE_TAG="${CAELUM_DOCKER_TEST}/caelum_qcon_dev:${CURRENT}"

docker build -t $RELEASE_TAG --file Dev .
