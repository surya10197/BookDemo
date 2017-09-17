# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
class Book(models.Model):
    currentTime = datetime.datetime.utcnow()
    name = models.CharField(max_length=100, verbose_name="Book  Name", unique=True)
    author = models.CharField(max_length=100, verbose_name="Book Author")
    content = models.CharField(verbose_name="Book Content", max_length=1000)
    created = models.DateTimeField(verbose_name="Book Creation Time", default=currentTime)
    expiry = models.DateTimeField(verbose_name="Book URL Expiry Time", default=currentTime + datetime.timedelta(seconds=60))
    

