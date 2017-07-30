FROM ubuntu:14.04
ARG port_to_expose

RUN apt-get update && \
    apt-get install -y ssh python-pip \
        libssl-dev libffi-dev \
        build-essential \
        git \
        nginx \
        python-virtualenv \
        python2.7 \
        python-dev \
        libjpeg-dev \
        libxml2-dev \
        libxslt1-dev \
        libfreetype6-dev \
        curl \
        libpq-dev && \
    rm -rf /var/lib/apt/lists

RUN pip install j2cli
COPY . /django_steps

COPY docker_templates /templates
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

RUN mkdir -p /var/log/uwsgi
RUN virtualenv -p /usr/bin/python2.7 /venv
RUN /venv/bin/pip install -r /django_steps/requirements.txt

EXPOSE $port_to_expose

ENTRYPOINT ["/entrypoint.sh"]
