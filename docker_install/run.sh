#!/bin/sh

# TODO XXX rewrite this with ansible docker one day
SECRET_VARS_FILE=secret_vars.yml

# build app container
sudo docker build -t app .

# collect env variables
env_vars=""
for env_var_line in $(cat "$SECRET_VARS_FILE" | sed 's/: /=/g'); 
do
    env_vars+="-e \"$env_var_line\" ";
done;

echo "$env_vars";

# run app container in background
eval  "sudo docker run -i -t -p 7777:7777 $env_vars app"
