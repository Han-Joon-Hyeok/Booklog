from django.urls import path
from .views import *

urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('detail/<str:id>', detail, name="detail"),
    path('edit/<str:id>', edit, name="edit"),
    path('add_comment_to_post/<str:id>', add_comment_to_post, name="add_comment_to_post"),
    # path('', home, name="home"),
]