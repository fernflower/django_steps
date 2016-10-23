A blog-like django-based website (Python 2, Django 1.6.5)

## Installation

### Custom settings in secret_vars.yml
Make your own secret_vars.yml file from sample and populate it.

```
cp docker_install/secret_vars_sample.yml docker_install/secret_vars.yml
```

### Running install script
Docker installation (assumes that you have docker and postgresql on host machine):
```
cd docker_install && bash docker_install/run.sh
```

[Here (deprecated)](https://github.com/fernflower/ansible_django_steps) you can find ansible playbook to ease the pain of deployment. Clone the repo and follow the installation guide.


## TODO list
- [] utilize ansible docker for docker installation
- [] postgresql in a docker container or configured by ansible on host
