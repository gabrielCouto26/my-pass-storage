#!bin/bash

COMMAND=$1
KEY=$2
VALUE=$3

docker run --rm \
    -e COMMAND=$COMMAND \
    -e KEY=$KEY \
    -e VALUE=$VALUE \
    -v ./storage.json:/usr/src/app/storage.json \
    pass-storage:latest