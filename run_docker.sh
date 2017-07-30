#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
SECRET_VARS_FILE="secret_vars.yml"
DATA_CONTAINER=data-cont
DB_CONTAINER=blog-db
IMAGE=blog
NAME=blog
ENV_FILE=blog.env

# get variables from secret_vars
NGINX_PORT=$(cat $SECRET_VARS_FILE | grep NGINX_PORT | sed 's/.*: //g')

# TODO maybe use KEY=VALUE in secret_vars rightaway?
# create env-file
cat "$SECRET_VARS_FILE" | sed 's/: /=/g' > $ENV_FILE
echo "DBHOST=$DB_CONTAINER" >> $ENV_FILE

sudo docker build --build-arg port_to_expose=$NGINX_PORT -t $IMAGE .
sudo docker run --name $NAME --link $DB_CONTAINER:postgres --volumes-from $DATA_CONTAINER -p $NGINX_PORT:$NGINX_PORT -dt --env-file $ENV_FILE $IMAGE
