#!/bin/bash -e

# pick up conf change
service nginx restart

/venv/bin/uwsgi --ini /django_steps/uwsgi_steps.ini
