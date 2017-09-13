FROM phusion/baseimage:0.9.22
ARG port_to_expose

COPY . /django_steps

RUN apt-get update && \
    apt-get install -y ssh python-pip \
        build-essential \
        git \
        nginx \
        python-virtualenv \
        python2.7 \
        python-dev &&\
    rm -rf /var/lib/apt/lists && \
    pip install j2cli && \
    chmod +x /django_steps/entrypoint.sh && \
    mkdir -p /var/log/uwsgi && \
    virtualenv -p /usr/bin/python2.7 /venv && \
    /venv/bin/pip install -r /django_steps/requirements.txt

CMD ["/sbin/my_init"]

EXPOSE $port_to_expose

ENTRYPOINT ["/django_steps/entrypoint.sh"]
