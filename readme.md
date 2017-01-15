A blog-like django-based website (Python 2, Django 1.6.5)

## Installation

### Custom settings in secret_vars.yml
Make your own secret_vars.yml file from sample and populate it.

```
cp secret_vars_sample.yml secret_vars.yml
```

### Running install script
Docker installation
The application is served by 3 containers: django/nginx, postgres and data.

Launch data container:
```
bash run_docker_data.sh
```

Launch postgres container:
```
bash run_docker_postgresql.sh
```

Launch django/nginx container:
```
bash run_docker.sh
```

[Here (deprecated)](https://github.com/fernflower/ansible_django_steps) you can find ansible playbook to ease the pain of deployment. Clone the repo and follow the installation guide.


## TODO list
- [] utilize ansible docker for docker installation
- [x] postgresql in a docker container or configured by ansible on host
- [] make deployment kubernetes-friendly
