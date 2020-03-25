#!/bin/sh
# TODO XXX rewrite this with ansible docker one day

ENV_FILE="blog.env"
IMAGE=blog
DEFAULT_NGINX_PORT=8888

source $ENV_FILE
CONTAINER_NAME="blog-$UNIQ_SUFFIX"

if [[ -z $NGINX_PORT ]]; then
    echo "NGINX_PORT is not defined, using default 8888"
    NGINX_PORT=$DEFAULT_NGINX_PORT
fi

sudo docker build --build-arg nginx_port=$NGINX_PORT -t $IMAGE .
sudo docker run --name $CONTAINER_NAME -p $NGINX_PORT:$NGINX_PORT -dt --env-file $ENV_FILE $IMAGE
