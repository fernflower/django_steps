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
    # FIXME some day a bootstrapped admin should appear, but currently it is
    # breaking VK Scraper link and wysiwyg post edition facilities
    # 'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'icons_famfamfam',
    'south',
    'admin_reorder',
    'django_markdown',
    'adminfiles',
    'sorl.thumbnail',
    'posts',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)

TEMPLATE_DIRS = (
    'posts/templates',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
)

ADMIN_REORDER = (
    # Rename app
    {'app': 'auth', 'label': 'Site Authorization'},
    # Keep original label and models
    'posts',
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
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': MY_DB_NAME,
        'USER': MY_DB_USER,
        'PASSWORD': MY_DB_PASSWORD,
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'common_static/'), )

# sentry configuration
RAVEN_CONFIG = MY_RAVEN_CONFIG

if RAVEN_CONFIG:
    INSTALLED_APPS = INSTALLED_APPS + \
        ('raven.contrib.django.raven_compat',)

# img-video and text cut settings
IMG_VIDEO_COUNT = 2
TEXT_CHARS_COUNT = 50
HTML_CUT_TEXT = u"(Читать дальше ...)"

# django-markdown
MARKDOWN_PREVIEW_TEMPLATE = "posts/preview.html"
