from django.shortcuts import render

# Create your views here.


def writeprofile(request):
    return render(request, 'writeProfile.html')


def profile(request):
    return render(request, "profile.html")
