#!/bin/bash -e

# create secret_settings.yml for django app
j2 /templates/secret_settings.j2 > /django_steps/mysite/mysite/secret_settings.py
cat /django_steps/mysite/mysite/secret_settings.py
# run syncd and apply migrations
/venv/bin/python /django_steps/mysite/manage.py syncdb --noinput
/venv/bin/python /django_steps/mysite/manage.py migrate posts
# create django admin user
/venv/bin/python /django_steps/mysite/change_admin_pass.py ina ina

# create nginx conf files
j2 /templates/nginx.j2 > /etc/nginx/sites-available/django
ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/django
service nginx restart

# create uswgi.ini and start uwsgi server
j2 /templates/uwsgi.j2 > /django_steps/uwsgi_steps.ini
/venv/bin/uwsgi --ini /django_steps/uwsgi_steps.ini &
# delete stale static files
rm -rf /django_steps/mysite/static
# regenerate static files
/venv/bin/python /django_steps/mysite/manage.py collectstatic --noinput

exec /bin/bash
