#!/bin/bash -e

# wait for postgres container to be up and running
# while ! curl http://$DBHOST:$DBPORT/ 2>&1 | grep '52'; do
#    sleep 1;
# done

# create nginx conf files
j2 /django_steps/docker_templates/nginx.j2 > /etc/nginx/sites-available/django
ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/django
service nginx restart

# create uswgi.ini and start uwsgi server
j2 /django_steps/docker_templates/uwsgi.j2 > /django_steps/uwsgi_steps.ini

# create config.ini from env vars
j2 /django_steps/docker_templates/config.j2 > /django_steps/mysite/config.ini

# compile translations
#/venv/bin/python pybabel compile -f -d ./locale

/venv/bin/uwsgi --ini /django_steps/uwsgi_steps.ini &
exec /bin/bash
