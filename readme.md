A blog-like bottle-based website in a container (Python 2, Bottle framework, nginx)

## Installation

### Custom settings in secret_vars.yml
Make your own blog.env file from sample and populate it.

```
cp blog.env.sample blog.env
```

### Running docker
The application is served by a single bottle/nginx container.

Launch it:
```
bash run_docker.sh
```

## TODO list
- [] utilize ansible docker for docker installation
- [] make deployment kubernetes-friendly
