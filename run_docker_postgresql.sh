#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
ENV_FILE="blog.env"
CONTAINER_NAME=blog-db
IMAGE=postgres
DATA_CONTAINER=data-cont

postgres_password=$(cat "$ENV_FILE" | grep DBPASS | sed 's/.*=//g');
postgres_user=$(cat "$ENV_FILE" | grep DBUSER | sed 's/.*=//g');
postgres_db=$(cat "$ENV_FILE" | grep DBNAME | sed 's/.*=//g');

sudo docker run -d --name $CONTAINER_NAME -e POSTGRES_PASSWORD=$postgres_password -e POSTGRES_DB=$postgres_db -e POSTGRES_USER=$postgres_user --volumes-from $DATA_CONTAINER $IMAGE
