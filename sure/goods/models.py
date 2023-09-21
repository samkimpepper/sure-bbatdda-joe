from django.db import models

# Create your models here.
from user.models import User

class Goods(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField()
    content = models.TextField(null=True)
    price = models.IntegerField()
    img = models.CharField()
    location = models.CharField()
    status = models.BooleanField(default=False)
    like_cnt = models.IntegerField(default=0)
    chat_cnt = models.IntegerField(default=0)
    upload_date = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)