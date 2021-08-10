# from django.db import models

# # Create your models here.

# ========= 기존에 코드가 재대로 실행이 안되었던 부분입니다.(기존작업물 업로드) ==========
# python manage.py makemigrations & migrate 안한 상태

from django.db import models
from user.models import *

# 팔로우
class Follow(models.Model):
    follower = models.ForeignKey('MyUser', related_name="follower", on_delete=models.CASCADE)
    following = models.ForeignKey('MyUser', related_name='follwing', on_delete=models.CASCADE)

    class Mata:
        db_table = 'follows'

# 좋아요
class Like(models.Model) :
    like_username = models.ForeignKey('user.MyUser', on_delete = models.CASCADE)
    #=== 좋아요 누르는 각각의 피드 입력해넣어야함. (app.Modes 이부분)====
    posting = models.ForeignKey("app.Model", on_delete=models.CASCADE)
    #===========================================================
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta :
        db_table='likes'