from django.shortcuts import redirect, render, get_object_or_404
from signup.models import MyUser
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth import get_user_model
from post.models import Post

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
            profile.image=request.FILES['image']
            profile.nickname = request.POST['nickname']
            profile.description = request.POST['description']
            print('저장하기')
            print('사진 : ',profile.image)
            print('이름 : ',profile.nickname)
            print('설명 : ',profile.description)
            profile.save()
            form.save()
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


def profile(request):
    profile = Profile.objects.get(user=MyUser.objects.get(name=request.user.name))
    print(1)
    cnt = Post.objects.filter(profile=profile).count()
    print(2)
    response_data = {}
    response_data["count"] = cnt
    print(4)
    response_data["profile"] = profile
    print(5)
    print(cnt)
    print()    
    print()    
    print()    
    print()    
    print()    

    # <test용
    # print(user.id)
    # print(user.username)
    # print(user.email)
    # print(profile.id)
    # print(profile.description)
    # test용>
    return render(request, "profile.html", response_data)


