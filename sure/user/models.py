from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username