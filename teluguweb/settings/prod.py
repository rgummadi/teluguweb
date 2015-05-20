# settings/prod.py
from .base import *

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://%s.s3.amazonaws.com/" % environ["S3_BUCKET"]

DEBUG = False



# =========
# = Mongo =
# =========

_MONGO_DB_NAME = 'heroku_app36456202'
_MONGO_URI = environ["MONGOLAB_URI"]

mongoengine.connect(_MONGO_DB_NAME, host=_MONGO_URI)