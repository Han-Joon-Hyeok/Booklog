from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/<str:id>', views.profile, name="profile"),
    path('writeProfile/<str:id>', views.writeprofile, name="writeprofile"),
    # path('writeProfile/<str:id>', pv.writeprofile, name="writeprofile"),
]
