from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=200)
  writer = models.CharField(max_length=100)
  pub_date = models.DateTimeField()
  body = models.TextField()

  def __str__(self):
      return self.title # 객체가 호출되면, 나오는 이름
      
  # 본문 요약 메소드
  def summary(self):
    return self.body[:100]