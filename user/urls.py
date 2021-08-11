from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:id>', views.profile, name="profile"),
    path('writeProfile/<int:pk>', views.writeprofile, name="writeprofile"),
    # path('writeProfile/<str:id>', pv.writeprofile, name="writeprofile"),
]