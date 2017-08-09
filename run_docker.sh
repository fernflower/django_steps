#!/bin/sh
# change this to form unique container name for your app
UNIQ_SUFFIX=ina

# XXX maybe proper deployment will fix this ambiguity
DATA_CONTAINER="data-cont-$UNIQ_SUFFIX"
DB_CONTAINER="blog-db-$UNIQ_SUFFIX"

# TODO XXX rewrite this with ansible docker one day
ENV_FILE="blog.env"
CONTAINER_NAME="blog-$UNIQ_SUFFIX"
IMAGE=blog

# get variables from secret_vars
nginx_port=$(cat $ENV_FILE | grep NGINX_PORT | sed 's/.*=//g')
nginx_host=$(cat $ENV_FILE | grep NGINX_HOST | sed 's/.*=//g')
postgres_user=$(cat "$ENV_FILE" | grep DBUSER | sed 's/.*=//g');
postgres_db=$(cat "$ENV_FILE" | grep DBNAME | sed 's/.*=//g');
db_posts_dump=$(cat $ENV_FILE | grep DB_DUMP | sed 's/.*=//g')

# add DBHOST container name to environment file
if ! [[ $(cat $ENV_FILE | grep DBHOST) ]]; then
    echo "DBHOST=$DB_CONTAINER" >> $ENV_FILE
fi

# add proper allowed hosts
if ! [[ $(cat $ENV_FILE | grep DJANGO_ALLOWED_HOSTS) ]]; then
    echo "DJANGO_ALLOWED_HOSTS=[\"$nginx_host\"]" >> $ENV_FILE
fi

sudo docker build --build-arg port_to_expose=$nginx_port -t $IMAGE .
sudo docker run --name $CONTAINER_NAME --link $DB_CONTAINER --volumes-from $DATA_CONTAINER -p $nginx_port:$nginx_port -dt --env-file $ENV_FILE $IMAGE
# for testing only
# sudo docker run --name $CONTAINER_NAME --link $DB_CONTAINER -v /home/ina/projects/django_steps/mysite/common_static/:/django_steps/mysite/common_static:ro -v /home/ina/projects/django_steps/mysite/posts/:/django_steps/mysite/posts:ro --volumes-from $DATA_CONTAINER -p $nginx_port:$nginx_port -it --env-file $ENV_FILE $IMAGE

# XXX FIXME TODO proper backup/restore technic
# restore db from a dump (table dump like one below)
# pg_dump --data-only --host localhost --port 5432 --username USER --format plain --ignore-version --verbose --file BACKUP --table TABKE DB
if [[ $db_posts_dump ]]; then
    cat $db_posts_dump | sudo docker exec -i $DB_CONTAINER psql $postgres_db $postgres_user
fi
