#!/bin/sh
IMAGE=busybox
NAME=data-cont
DIR=/var/lib/postgresql

sudo docker create --name $NAME -v $DIR --name $NAME $IMAGE /bin/true
