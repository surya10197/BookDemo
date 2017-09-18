# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from django.utils import timezone
from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Book(models.Model):
    currentTime = datetime.now
    name = models.CharField(max_length=100, verbose_name="Book  Name", unique=True)
    author = models.CharField(max_length=100, verbose_name="Book Author")
    content = models.CharField(verbose_name="Book Content", max_length=1000)
    created = models.DateTimeField(verbose_name="Book Creation Time", default=currentTime)
    #expiry = models.DateTimeField(verbose_name="Book URL Expiry Time", default=(currentTime + timedelta(seconds=60)))
    

