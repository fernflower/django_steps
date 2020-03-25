A blog-like bottle-based website in a container (Python 2, Bottle framework, nginx)

## Installation

### Custom settings in secret_vars.yml
Make your own blog.env file from sample and populate it.

```
cp blog.env.sample blog.env
```

### Running docker
The application is served by a single bottle/nginx container.

You can build and run it using docker-compose `docker-compose up -d` or
plain old bash-script-it way `bash run_docker.sh`.

If you haven't changed the defaults in blog.env the site will be served
at http://localhost:8888

## TODO list
- [x] docker-compose for easy deployment
- [] make deployment kubernetes-friendly
