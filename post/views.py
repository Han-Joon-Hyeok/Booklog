from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from django.utils import timezone

def home(request):
  # Post table에 있는 객체들을 가져와서 posts에 저장
  posts = Post.objects.all()
  return render(request, "home.html", {'posts':posts})

def detail(request, id):
  post = get_object_or_404(Post, pk=id)
  return render(request, "detail.html", {'post':post})

def new(request):
  return render(request, "new.html")

def create(request):
  # new.html에서 작성한 정보를 받아서 저장함
  new_post = Post()
  new_post.title = request.POST['title']
  new_post.writer = request.POST['writer']
  new_post.body = request.POST['body']
  new_post.pub_date = timezone.now() # 작성한 현재 시각
  new_post.save()
  return redirect('detail', new_post.id)

def edit(request, id):
  edit_post = Post.objects.get(id=id)
  return render(request, 'edit.html',{'post':edit_post})

def update(request, id):
  update_post = Post.objects.get(id=id)
  update_post.title = request.POST['title']
  update_post.writer = request.POST['writer']
  update_post.body = request.POST['body']
  update_post.pub_date = timezone.now() 
  update_post.save()
  return redirect('detail', update_post.id)

def delete(request, id):
  delete_post = Post.objects.get(id=id)
  delete_post.delete()
  return redirect('home')
