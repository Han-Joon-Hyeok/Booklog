from django.db import models
# from signup.models import MyUser

class Profile(models.Model):
    # # # User모델과 Profile을 1:1로 연결
    # user = models.OneToOneField(MyUser, default=None, null=True, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40, blank=True,  default='')
    image = models.ImageField(blank=True,  default='', null=True)
    description = models.TextField(blank=True, default='', null=True )

    def __str__(self): #어디선가 객체가 호출될떄의 이름표설정하는 것과 같음.
        return self.nickname
