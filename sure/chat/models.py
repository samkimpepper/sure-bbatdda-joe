from django.db import models

# Create your models here.
from user.models import User 
from goods.models import Goods

class Chat(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_chat')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_chat')

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    send_date = models.DateTimeField()
    status = models.BooleanField()
    img = models.CharField(null=True)