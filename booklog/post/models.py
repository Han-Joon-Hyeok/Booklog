from django.db import models
from django.utils import timezone

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


class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='comments',
  on_delete=models.CASCADE)
  author_name = models.CharField(max_length=20)
  comment_text = models.TextField()
  created_at = models.DateTimeField(default=timezone.now) # 장고에서 기본으로 제공

  # 들어갈 내용들 : 댓글 작성자, 댓글 내용, 댓글 작성 시간

  def approve(self):
    self.save()

  def __str__(self):
    return self.comment_text
