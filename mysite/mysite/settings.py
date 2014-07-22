"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from contacts.secret_settings import * # NOQA


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
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap',
    'django_summernote',
    'captcha',
    'icons_famfamfam',
    'about',
    'contacts',
    'posts',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

LOGGING = {
    'version': 1,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = MY_EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = MY_EMAIL_HOST_PASSWORD
EMAIL_RECIPIENT_LIST = MY_EMAIL_RECIPIENT_LIST

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

VK_API_ID = MY_VK_API_ID

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
