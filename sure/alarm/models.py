from django.db import models

# Create your models here.
from user.models import User 
from chat.models import Message

class Alarm(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)