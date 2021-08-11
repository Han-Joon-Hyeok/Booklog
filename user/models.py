from signup.models import MyUser
from django.db import models
# from django.conf import settings
from signup.models import MyUser
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    # # User모델과 Profile을 1:1로 연결
    image = models.ImageField(blank=True,  default='')
    nickname = models.CharField(max_length=40, blank=True,  default='')
    description = models.TextField(blank=True, default='')