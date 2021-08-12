from io import open_code
from user.models import Profile
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    name = models.CharField(max_length=30)
    profile = models.OneToOneField(Profile, default=None, null=True, on_delete=models.CASCADE)


