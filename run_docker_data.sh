#!/bin/sh
IMAGE=busybox
NAME=data-cont
DIR=/var/lib/postgresql

sudo docker run --name $NAME -v $DIR --name $NAME $IMAGE echo 'data container started!'
