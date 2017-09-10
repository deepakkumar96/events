from django.db import models
# from __future__ import unicode_literals
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from .managers import AccountManager
from CollegeEvents3 import settings


class MyUser(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Event(models.Model):
    user = models.ForeignKey(MyUser, related_name='events')
    event_name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.event_name






