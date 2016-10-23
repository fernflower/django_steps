#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SECRET_VARS_FILE="$DIR/secret_vars.yml"
IMAGE=app

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
run_cmd=$(printf "sudo docker run -i -d -t -p 7777:7777 %s %s" "$env_vars" "$IMAGE")
eval $run_cmd

echo "$IMAGE can be accessed at $(sudo docker ps -f image=\"$IMAGE\" | grep -oP '[0-9.:]*->' | sed 's/->//')"

