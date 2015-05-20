# local.py
from .base import *

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://%s.s3.amazonaws.com/" % environ["S3_BUCKET"]

# print(STATIC_URL)

DEBUG = True


# =========
# = Mongo =
# =========
_MONGO_DB_NAME = 'teluguweb'
mongoengine.connect(_MONGO_DB_NAME)