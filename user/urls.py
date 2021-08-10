from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('writeProfile/', views.writeprofile, name="writeprofile"),
    # path('writeProfile/<str:id>', pv.writeprofile, name="writeprofile"),
]