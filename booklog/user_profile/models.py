from django.db import models
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # # User모델과 Profile을 1:1로 연결
    image = models.ImageField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)