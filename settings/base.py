"""
Django settings for teluguweb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import join, abspath, dirname
from os import environ
import mongoengine

# ===========================
# = Directory Declarations =
# ===========================

BASE_DIR = dirname(dirname(dirname(__file__)))


#print(BASE_DIR)



# STATIC_URL = '/static/'
TEMPLATES_DIR = (join(BASE_DIR,'apps/mainsite/templates/'),)
STATICFILES_DIRS = (join(BASE_DIR, "app/mainsite/static/"),)

#print(STATICFILES_DIRS)


AWS_STORAGE_BUCKET_NAME = environ["S3_BUCKET"]
AWS_ACCESS_KEY_ID = environ["AWS_ACCESS_KEY"]
AWS_SECRET_ACCESS_KEY = environ["AWS_SECRET_KEY"]


#print (BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'im*k0tlqdz$#aok#3v$m3%lmrj@#r6tctxxu81l_(74r_8q&3r'


# SECURITY WARNING: don't run with debug turned on in production!

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
    'apps.mainsite',
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

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


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




# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/






