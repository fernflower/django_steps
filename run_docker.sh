#!/bin/sh
# change this to form unique container name for your app
UNIQ_SUFFIX=max

# TODO XXX rewrite this with ansible docker one day
ENV_FILE="blog.env"
CONTAINER_NAME="blog-$UNIQ_SUFFIX"
IMAGE=blog

# get variables from secret_vars
nginx_port=$(cat $ENV_FILE | grep NGINX_PORT | sed 's/.*=//g')
nginx_host=$(cat $ENV_FILE | grep NGINX_HOST | sed 's/.*=//g')

# add proper allowed hosts
if ! [[ $(cat $ENV_FILE | grep DJANGO_ALLOWED_HOSTS) ]]; then
    echo "DJANGO_ALLOWED_HOSTS=[\"$nginx_host\"]" >> $ENV_FILE
fi

sudo docker build --build-arg port_to_expose=$nginx_port -t $IMAGE .
sudo docker run --name $CONTAINER_NAME -p $nginx_port:$nginx_port -it --env-file $ENV_FILE $IMAGE
# for testing only
# sudo docker run --name $CONTAINER_NAME -v /home/ina/projects/django_steps/mysite/common_static/:/django_steps/mysite/common_static:ro -v /home/ina/projects/django_steps/mysite/posts/:/django_steps/mysite/posts:ro -p $nginx_port:$nginx_port -it --env-file $ENV_FILE $IMAGE
