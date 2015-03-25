from django.db import models
from mongoengine import *

# Create your models here.

class Links(Document):
    weight = IntField()
    imageurl = StringField()
    desc = StringField()
    mindesc = StringField()
    imagepath =  StringField()
    title = StringField()
    url = URLField()
    insertdate = DateTimeField()
    insertdatetime = DateTimeField()
    source = StringField()
    engsource = StringField()

