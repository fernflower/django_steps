#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
ENV_FILE="blog.env"
CONTAINER_NAME=blog
IMAGE=blog
DATA_CONTAINER=data-cont
DB_CONTAINER=blog-db

# get variables from secret_vars
nginx_port=$(cat $ENV_FILE | grep NGINX_PORT | sed 's/.*=//g')
postgres_user=$(cat "$ENV_FILE" | grep DBUSER | sed 's/.*=//g');
postgres_db=$(cat "$ENV_FILE" | grep DBNAME | sed 's/.*=//g');
db_posts_dump=$(cat $ENV_FILE | grep DB_DUMP | sed 's/.*=//g')

# add DBHOST container name to environment file
if ! [[ $(cat $ENV_FILE | grep DBHOST) ]]; then
    echo "DBHOST=$DB_CONTAINER" >> $ENV_FILE
fi

sudo docker build --build-arg port_to_expose=$nginx_port -t $IMAGE .
sudo docker run --name $CONTAINER_NAME --link $DB_CONTAINER --volumes-from $DATA_CONTAINER -p $nginx_port:$nginx_port -dt --env-file $ENV_FILE $IMAGE

# XXX FIXME TODO proper backup/restore technic
# restore db from a dump (table dump like one below)
# pg_dump --data-only --host localhost --port 5432 --username USER --format plain --ignore-version --verbose --file BACKUP --table TABKE DB
if [[ $db_posts_dump ]]; then
    cat $db_posts_dump | sudo docker exec -i $DB_CONTAINER psql $postgres_db $postgres_user
fi
