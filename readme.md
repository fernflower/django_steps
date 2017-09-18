A blog-like bottle-based website in a container (Python 2, Bottle framework, nginx)

## Installation

### Custom settings in secret_vars.yml
Make your own blog.env file from sample and populate it.

```
cp blog.env.sample blog.env
```

### Running install script
Docker installation
The application is served by 3 containers: django/nginx, postgres and data.

Launch bottle/nginx container:
```
bash run_docker.sh
```

## TODO list
- [] utilize ansible docker for docker installation
- [] make deployment kubernetes-friendly
