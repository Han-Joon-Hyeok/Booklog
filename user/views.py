from django.shortcuts import redirect, render, get_object_or_404
from signup.models import MyUser
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import get_user_model

# Create your views here.

def writeprofile(request, id):
    user = MyUser.objects.get(id=id)
    if Profile.objects.get_or_create(id=id):
        profile = Profile.objects.get(id=id)
    else:
        profile = Profile    

    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            # clean data
            profile.image = request.POST['image']
            profile.nickname = request.POST['nickname']
            profile.description = request.POST['description']
            print('저장하기')
            print('사진 : ',profile.image)
            print('이름 : ',profile.nickname)
            print('설명 : ',profile.description)
            profile.save()
            return redirect('profile',user.id)
    else:
        # login 쪽에서 이메일이랑 아이디 가져와야함.
        context = {
            'user':user,
            'profile':profile,
        }   
        print('불러오기')
        print('사진 : ',profile.image)
        print('이름 : ',profile.nickname)
        print('설명 : ',profile.description)
        return render(request, "writeProfile.html", context)


def profile(request,id):
    user = MyUser.objects.get(id=id)
    if Profile.objects.get_or_create(id=id):
        profile = Profile.objects.get(id=id)
    else:
        profile = Profile    
    context = {
        'user':user,
        'profile':profile,
    }
    return render(request, "profile.html", context)


