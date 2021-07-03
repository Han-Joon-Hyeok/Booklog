from django.shortcuts import redirect, render
from .models import Profile
from .forms import ProfileForm

# Create your views here.



# def writeprofile(request, id):
def writeprofile(request):
    if request.method =='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            # clean data
            profile = Profile()
            # profile = Profile.objects.get(id=id)
            profile.image = request.POST['image']
            profile.nickname = request.POST['nickname']
            profile.description = request.POST['description']
            profile.save()
            print()
            return redirect('profile')
    # else:
        # login 쪽에서 이메일이랑 아이디 가져와야함.
    return render(request, 'writeprofile.html' )



def profile(request):
    return render(request, "profile.html")


