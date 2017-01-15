#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
SECRET_VARS_FILE="secret_vars.yml"
DATA_CONTAINER=data-cont
IMAGE=blog
NAME=blog

# build $IMAGE container
sudo docker build -t "$IMAGE" .

# collect env variables
env_vars=""
for env_var_line in $(cat "$SECRET_VARS_FILE" | sed 's/: /=/g'); 
do
    env_vars+="-e \"$env_var_line\" ";
done;

# XXX FIXME This bloody eval is the workaround for the first -e in env_vars
# to be treated as docker run command param (otherwise it's swallowed by bash).
run_cmd=$(printf "sudo docker run --name $NAME --link blog-db:postgres --volumes-from $DATA_CONTAINER -i -t -p 7777:7777 %s %s" "$env_vars" "$IMAGE")
eval $run_cmd
