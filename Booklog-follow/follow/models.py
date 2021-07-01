from django.db import models

# Create your models here.
# 팔로우
class Follow(models.Model):
    follower = models.ForeignKey('MyUser', related_name="follower", on_delete=models.CASCADE)
    following = models.ForeignKey('MyUser', related_name='follwing', on_delete=models.CASCADE)

    class Mata:
        db_table = 'follows'

# 좋아요
class Like(models.Model) :
    like_username = models.ForeignKey('myuser.MyUser', on_delete = models.CASCADE)
    #=== 좋아요 누르는 각각의 피드 입력해넣어야함. (app.Modes 이부분)====
    posting = models.ForeignKey("app.Model", on_delete=models.CASCADE)
    #===========================================================
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta :
        db_table='likes'