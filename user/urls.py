from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('writeProfile/', views.writeprofile, name="writeprofile"),
    path('saveProfile/<str:id>', views.saveProfile, name="saveProfile"),
]
