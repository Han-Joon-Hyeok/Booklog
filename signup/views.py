from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import MyUser
from user.models import Profile


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/',{'user':user})        # login성공되면 필요시 경로 수정! 현재 기본은 home화면이 되어있다. # 프로필페이지 연결테스트를 위해 {user:user}추가함. -수정
        else:
            print("login fail")
            return render(request, "login.html", {'error': True})

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if name != '' and email != '' and username != '' and password1 != '' and password2 != '':
            if password1 == password2:
                user = MyUser.objects.create_user(username, email, password1)
                user.name = name
                user.save()
                # Profile(user=user).save()
                # print("sign up success")
                # return redirect('login')
                return redirect("login")
            else:
                print('wrong password')

    return render(request, "signup.html")

