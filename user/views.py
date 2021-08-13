from django.shortcuts import redirect, render, get_object_or_404
from signup.models import MyUser
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import get_user_model
from post.models import Post

# Create your views here.

def writeprofile(request):
    id =request.user.id
    user = MyUser.objects.get(id=id)
    if Profile.objects.get_or_create(id=id):
        profile = Profile.objects.get(id=id)
    else:
        profile = Profile    
        
    if request.method =='GET':
        # login 쪽에서 이메일이랑 아이디 가져와야함.
        response_data = {
            'user':user,
            'profile':profile,
        }   
        return render(request, "writeProfile.html", response_data)

def saveProfile(request, id):
    user = MyUser.objects.get(id=id)
    if Profile.objects.get_or_create(id=id):
        profile = Profile.objects.get(id=id)
    else:
        profile = Profile    

    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            # clean data
            profile.image=request.FILES['image']
            profile.nickname = request.POST['nickname']
            profile.description = request.POST['description']
            profile.save()
            form.save()
    response_data = {
        'user':user,
        'profile':profile,
        'cnt':Post.objects.filter(user=user).count(),
    }   
    return render(request, "profile.html", response_data)

def profile(request):
    user=MyUser.objects.get(id=request.user.id)
    if Profile.objects.get_or_create(id=request.user.id):
        profile = Profile.objects.get(id=request.user.id)
    else:
        profile = Profile    
    cnt = Post.objects.filter(user=user).count()
    # response_data = {}
    # response_data["count"] = cnt
    # response_data["profile"] = profile
    response_data = {
        'user':user,
        'profile':profile,
        'cnt':cnt,
    }   
    request.user = user
    request.profile = profile
    request.cnt = cnt
    return render(request, "profile.html", response_data)


