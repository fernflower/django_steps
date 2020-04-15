FROM phusion/baseimage:0.9.22
ARG nginx_port=8888
ENV NGINX_PORT=$nginx_port
ENV NGINX_HOST=0.0.0.0
ENV STATIC_URL=max_static
ENV EMAIL_CREDENTIALS_FILE=common_static/files/credentials.json
ENV EMAIL_TOKEN_FILE=common_static/files/token_email.pickle
ENV EMAIL_RECIPIENT_LIST=NOONE@gmail.com,

RUN apt-get update && \
    apt-get install -y ssh python3-pip \
        build-essential \
        python3-venv \
        git \
        nginx \
        python3.4 \
        python-dev && \
    rm -rf /var/lib/apt/lists && \
    pip3 install j2cli

CMD ["/sbin/my_init"]

COPY . /django_steps
RUN chmod +x /django_steps/entrypoint.sh && \
    mkdir -p /var/log/uwsgi && \
    python3 -m venv /venv && \
    /venv/bin/pip install -r /django_steps/requirements.txt

# create nginx conf files
RUN j2 /django_steps/docker_templates/nginx.j2 > /etc/nginx/sites-available/maxmakagonov
RUN ln -s /etc/nginx/sites-available/maxmakagonov /etc/nginx/sites-enabled/maxmakagonov

# create uswgi.ini and start uwsgi server
RUN j2 /django_steps/docker_templates/uwsgi.j2 > /django_steps/uwsgi_steps.ini

EXPOSE $NGINX_PORT

ENTRYPOINT ["/django_steps/entrypoint.sh"]
