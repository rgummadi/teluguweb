"""
Django settings for teluguweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import mongoengine


#print (BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'im*k0tlqdz$#aok#3v$m3%lmrj@#r6tctxxu81l_(74r_8q&3r'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost','teluguweb.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'teluguwebapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'teluguweb.urls'

WSGI_APPLICATION = 'teluguweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

# =========
# = Mongo =
# =========

_MONGO_DB_NAME = 'heroku_app36456202'
_MONGO_URI = os.environ["MONGOLAB_URI"]

mongoengine.connect(_MONGO_DB_NAME, host=_MONGO_URI)


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


# ===========================
# = Directory Declaractions =
# ===========================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# STATIC_URL = '/static/'
TEMPLATES_DIR = (os.path.join(BASE_DIR,'teluguwebapp/templates/'),)
# STATICFILES_DIRS = "s3://%s/" % os.environ["S3_BUCKET"]
STATICFILES_DIRS = (os.path.join(BASE_DIR, "teluguwebapp/static/"),)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://%s.s3.amazonaws.com/" % os.environ["S3_BUCKET"]

AWS_STORAGE_BUCKET_NAME = os.environ["S3_BUCKET"]
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_KEY"]
