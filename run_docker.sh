#!/bin/sh
# TODO XXX rewrite this with ansible docker one day

ENV_FILE="blog.env"
IMAGE=blog
UNIQ_SUFFIX=$(cat $ENV_FILE | grep "UNIQ_SUFFIX" | sed 's/.*=//g')
CONTAINER_NAME="blog-$UNIQ_SUFFIX"

# get variables from secret_vars
nginx_port=$(cat $ENV_FILE | grep NGINX_PORT | sed 's/.*=//g')
nginx_host=$(cat $ENV_FILE | grep NGINX_HOST | sed 's/.*=//g')


sudo docker build --build-arg port_to_expose=$nginx_port -t $IMAGE .
sudo docker run --name $CONTAINER_NAME -p $nginx_port:$nginx_port -it --env-file $ENV_FILE $IMAGE
