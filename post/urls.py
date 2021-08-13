from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name="home"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('detail/<str:id>', detail, name="detail"),
    path('edit/<str:id>', edit, name="edit"),
    path('add_comment_to_post/<str:id>', add_comment_to_post, name="add_comment_to_post"),
    path('update/<str:id>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
    path('search/', search, name='search'),
    path('count/', postCnt, name="postCnt")
]



#     path('', home, name="home"),
#     path('<str:id>', detail, name="detail"),
#     path('new/', new, name="new"),
#     path('create/', create, name="create"),
#     path('edit/<str:id>', edit, name="edit"),
#     path('update/<str:id>', update, name="update"),
#     path('delete/<str:id>', delete, name="delete"),
#     path('post/comment/<str:id>', add_comment_to_post, name='add_comment_to_post'),
#     path('search/', search, name='search'),
#     path('main/', main, name='main'),