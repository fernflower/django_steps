FROM phusion/baseimage:0.9.22
ARG port_to_expose

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

EXPOSE $port_to_expose

COPY . /django_steps
RUN chmod +x /django_steps/entrypoint.sh && \
    mkdir -p /var/log/uwsgi && \
    python3 -m venv /venv && \
    /venv/bin/pip install -r /django_steps/requirements.txt

ENTRYPOINT ["/django_steps/entrypoint.sh"]
