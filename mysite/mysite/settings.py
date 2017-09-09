# -*- coding: utf-8 -*-
"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from .secret_settings import * # NOQA


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'), )


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = MY_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = MY_DEBUG

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = MY_ALLOWED_HOSTS

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/posts/media/'


# Application definition


INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'posts',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    'posts/templates/posts',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {'level': 'DEBUG', 'class': 'logging.StreamHandler'},
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = MY_EMAIL_HOST
EMAIL_PORT = MY_EMAIL_PORT
EMAIL_HOST_USER = MY_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = MY_EMAIL_HOST_PASSWORD
EMAIL_RECIPIENT_LIST = MY_EMAIL_RECIPIENT_LIST

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
ugettext = lambda s: s
LANGUAGES = (('en', ugettext('English')),
             ('ru', ugettext('Russian')),)

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = MY_STATIC_URL
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'common_static/'), )

VIDEOS_FILE = (os.path.join(STATICFILES_DIRS[0], 'videos.txt'))
VIDEOS_PER_BLOCK = 9
