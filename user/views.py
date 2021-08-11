from django.shortcuts import redirect, render, get_object_or_404
from signup.models import MyUser
from .forms import ProfileForm
from django.contrib.auth import get_user_model

# Create your views here.

# def writeprofile(request, id):
#     print('id씀-----------------------------------------------')
#     User = get_user_model()
#     user = get_object_or_404(User, id=id)
#     context = {
#         'user': user,
#         'profile':profile
#     }
#     return render(request, 'writeprofile.html', context)


def writeprofile(request, id):
    user = MyUser.objects.get(id=id)
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            # clean data
            profile.image = request.POST['image']
            profile.nickname = request.POST['nickname']
            profile.description = request.POST['description']
            profile.save()
            return redirect('profile',id)
    else:
        # login 쪽에서 이메일이랑 아이디 가져와야함.
        print('test')
        context = {
        'user':user,
        'profile':profile,
        }
        return render(request, "writeProfile.html", context)


def profile(request,id):
    user = MyUser.objects.get(id=id)
    context = {
        'user':user,
        'profile':profile,
    }
    # <test용
    # print(user.id)
    # print(user.username)
    # print(user.email)
    # print(profile.id)
    # print(profile.description)
    # test용>
    return render(request, "profile.html", context)


