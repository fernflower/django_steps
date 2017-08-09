#!/bin/sh
# change this to form unique container name for your app
UNIQ_SUFFIX=ina

IMAGE=busybox
CONTAINER_NAME="data-cont-$UNIQ_SUFFIX"
DIR=/var/lib/postgresql

sudo docker create --name $CONTAINER_NAME -v $DIR $IMAGE /bin/true
