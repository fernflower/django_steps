#!/bin/sh
# change this to form unique container name for your app
UNIQ_SUFFIX=ina

# XXX maybe proper deployment will fix this ambiguity
DATA_CONTAINER="data-cont-$UNIQ_SUFFIX"

# TODO XXX rewrite this with ansible docker one day
ENV_FILE="blog.env"
CONTAINER_NAME="blog-db-$UNIQ_SUFFIX"
IMAGE=postgres

postgres_password=$(cat "$ENV_FILE" | grep DBPASS | sed 's/.*=//g');
postgres_user=$(cat "$ENV_FILE" | grep DBUSER | sed 's/.*=//g');
postgres_db=$(cat "$ENV_FILE" | grep DBNAME | sed 's/.*=//g');

sudo docker run -d --name $CONTAINER_NAME -e POSTGRES_PASSWORD=$postgres_password -e POSTGRES_DB=$postgres_db -e POSTGRES_USER=$postgres_user --volumes-from $DATA_CONTAINER $IMAGE
