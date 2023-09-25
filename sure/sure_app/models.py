from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    manner_tmp = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    
class Goods(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()
    content = models.TextField()
    price = models.IntegerField()
    img = models.TextField()
    location = models.CharField()
    status = models.BooleanField(default=False)
    like_cnt = models.IntegerField(default=0)
    chat_cnt = models.IntegerField(default=0)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    view_cnt = models.IntegerField(default=0) #조회수 컬럼 추가 by 오준경

class Like(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Chat(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_chat')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_chat')

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_message', default=None)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_message', default=None)
    text = models.TextField()
    status = models.BooleanField()
    img = models.TextField()
    send_date = models.DateTimeField()

class Alarm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

