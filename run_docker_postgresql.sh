#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
SECRET_VARS_FILE="secret_vars.yml"
IMAGE=postgres
NAME=blog-db
DATA_CONTAINER=data-cont

postgres_password=$(cat "$SECRET_VARS_FILE" | grep DBPASS | sed 's/.*: //g');
postgres_user=$(cat "$SECRET_VARS_FILE" | grep DBUSER | sed 's/.*: //g');
postgres_db=$(cat "$SECRET_VARS_FILE" | grep DBNAME | sed 's/.*: //g');

sudo docker run --name $NAME -e POSTGRES_PASSWORD=$postgres_password -e POSTGRES_DB=$postgres_db -e POSTGRES_USER=$postgres_user --volumes-from $DATA_CONTAINER $IMAGE
