#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
SECRET_VARS_FILE="secret_vars.yml"
DATA_CONTAINER=data-cont
DB_CONTAINER=blog-db
DB_PORT=5432
IMAGE=blog
NAME=blog

# build $IMAGE container
sudo docker build -t "$IMAGE" .

# collect env variables
env_vars="-e \"DBHOST=$DB_CONTAINER\" -e \"DBPORT=$DB_PORT\" "
for env_var_line in $(cat "$SECRET_VARS_FILE" | sed 's/: /=/g'); 
do
    env_vars+="-e \"$env_var_line\" ";
done;

# XXX FIXME This bloody eval is the workaround for the first -e in env_vars
# to be treated as docker run command param (otherwise it's swallowed by bash).
postgres_cont_ip=$(sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' blog-db)
run_cmd=$(printf "sudo docker run --name $NAME --link $DB_CONTAINER:postgres --volumes-from $DATA_CONTAINER -p 80:80 -d -t %s %s" "$env_vars" "$IMAGE")
eval $run_cmd
