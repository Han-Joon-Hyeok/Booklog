from django.shortcuts import redirect, render, get_object_or_404
from .models import Profile
from signup.models import MyUser
from .forms import ProfileForm
from django.contrib.auth import get_user_model

# Create your views here.

# def writeprofile(request, id):
#     print('id씀-----------------------------------------------')
#     User = get_user_model()
#     user = get_object_or_404(User, id=id)
#     profile = Profile.objects.get(id=id)
#     context = {
#         'user': user,
#         'profile':profile
#     }
#     return render(request, 'writeprofile.html', context)


def writeprofile(request, id):
# def writeprofile(request):
    print('id안씀-----------------------------------------------')
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            # clean data
            # profile = Profile()
            profile = Profile.objects.get(id=id)
            profile.image = request.POST['image']
            profile.nickname = request.POST['nickname']
            profile.description = request.POST['description']
            profile.save()
            return redirect('profile')
            # return render(request,'profile',id=id)
    else:
        # login 쪽에서 이메일이랑 아이디 가져와야함.
        myuser = MyUser.objects.get(id=id)
        context ={
            # 'profile':profile,
            'myuser':myuser,
        }
        return redirect('writeprofile',id)


def profile(request):
    User = get_user_model()
    user = get_object_or_404(User)
    context = {
        'user': user
    }
    return render(request, "profile.html", context)
        # profile = Profile.objects.get(id=id)



def profile(request,id):
    user = MyUser.objects.get(id=id)
    profile = Profile.objects.get(id=id)
    context = {
        'user':user,
        'profile':profile,
    }
    return render(request, "profile.html", context)


