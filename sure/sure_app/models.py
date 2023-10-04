from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    manner_tmp = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.CharField(null=True, max_length=100)
    location_certification = models.CharField(max_length=1, default='N')
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username
    
    
class Goods(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='uploads/')
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    like_cnt = models.IntegerField(default=0)
    chat_cnt = models.IntegerField(default=0)
    uploaded_date = models.DateTimeField(auto_now_add=True)
    view_cnt = models.IntegerField(default=0) #조회수 컬럼 추가 by 오준경
    def __str__(self):
        return self.title

class Like(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Chat(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buyer_chat')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_chat')

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_message', default=None, null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_message', default=None, null=True)
    text = models.TextField()
    status = models.BooleanField(default=False)
    img = models.TextField(null=True)
    send_date = models.DateTimeField(auto_now_add=True, null=True)

class Alarm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)
    content = models.CharField(max_length=50, null=True)
    link = models.TextField(null=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Review(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_review')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_review')
    content = models.TextField()
    manner_score = models.IntegerField() # 3 최고에요, 2 좋아요, 1 별로에요
    created_at = models.DateTimeField(auto_now_add=True)


