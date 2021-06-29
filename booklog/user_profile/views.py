from django.shortcuts import render

# Create your views here.

def writeprofile(request):
    return render(request, 'writeProfile.html')
