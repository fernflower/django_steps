#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
SECRET_VARS_FILE="secret_vars.yml"
DATA_CONTAINER=data-cont
DB_CONTAINER=blog-db
IMAGE=blog
NAME=blog
ENV_FILE=blog.env

# get variables from secret_vars
nginx_port=$(cat $SECRET_VARS_FILE | grep NGINX_PORT | sed 's/.*: //g')
postgres_user=$(cat "$SECRET_VARS_FILE" | grep DBUSER | sed 's/.*: //g');
postgres_db=$(cat "$SECRET_VARS_FILE" | grep DBNAME | sed 's/.*: //g');
db_posts_dump=$(cat $SECRET_VARS_FILE | grep DB_DUMP | sed 's/.*: //g')

# TODO maybe use KEY=VALUE in secret_vars rightaway?
# create env-file
cat "$SECRET_VARS_FILE" | sed 's/: /=/g' > $ENV_FILE
echo "DBHOST=$DB_CONTAINER" >> $ENV_FILE

sudo docker build --build-arg port_to_expose=$NGINX_PORT -t $IMAGE .
sudo docker run --name $NAME --link $DB_CONTAINER:postgres --volumes-from $DATA_CONTAINER -p $nginx_port:$nginx_port -dt --env-file $ENV_FILE $IMAGE

# XXX FIXME TODO proper backup/restore technic
# restore db from a dump (table dump like one below)
# pg_dump --data-only --host localhost --port 5432 --username USER --format plain --ignore-version --verbose --file BACKUP --table TABKE DB
if [[ $db_posts_dump ]]; then
    cat $db_posts_dump | sudo docker exec -i $DB_CONTAINER psql $postgres_db $postgres_user
fi
