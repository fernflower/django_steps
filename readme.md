A blog-like bottle-based website in a container (Python 2, Bottle framework, nginx)

For preview of the end result visit <https://maxmakagonov.com>

## Installation

### Initial setup
Make your own blog.env file from sample and populate it.

```
cp blog.env.sample blog.env
```
Leaving out customization for later should do.

### Running docker
The application is served by a single bottle/nginx container.

You can build and run it using docker-compose `docker-compose up -d` or
plain old bash-script-it way `bash run_docker.sh`.

If you haven't changed the defaults in blog.env the site will be served
at http://localhost:8888

## Deployment via ansible

For ansible deployment see <https://github.com/fernflower/django-steps-vm>.

## Google calendar events fetcher

The django_steps/fetchevents.py can be used to retrieve events from google calendar. Having the application secret is
the only prerequisite (not included here for good reasons).

## TODO list
- [x] docker-compose for easy deployment
- [ ] make deployment [kubernetes-friendly](https://twitter.com/dexhorthy/status/856639005462417409)
