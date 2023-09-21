from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils import timezone 


# Create your models here.

class User(AbstractUser):
    manner_tmp = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username