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

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#print (BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'im*k0tlqdz$#aok#3v$m3%lmrj@#r6tctxxu81l_(74r_8q&3r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

_MONGO_HOST = 'localhost'
_MONGO_DB_NAME = 'heroku_app35242924' #'teluguweb'
_MONGO_DB_HOST = \
    'mongodb://%s' \
    %(_MONGO_HOST,)
_MONGO_URI = "mongodb://heroku_app35242924:90s0k6rnu5a9iulpc1lqbf3327@ds059471.mongolab.com:59471/heroku_app35242924"
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

STATIC_URL = '/static/'
TEMPLATES_DIR = (os.path.join(BASE_DIR,'teluguwebapp/templates/'),)
STATICFILES_DIRS = (os.path.join(BASE_DIR, "teluguwebapp/static/"),)
#STATIC_ROOT = '/Users/rgummadi/Dropbox/WWW/dev/teluguweb/teluguwebapp/static/'

