#!/bin/bash -e

# pick up conf change
service nginx restart

# create config.ini from env vars
j2 /django_steps/docker_templates/config.j2 > /django_steps/mysite/config.ini

/venv/bin/uwsgi --ini /django_steps/uwsgi_steps.ini
