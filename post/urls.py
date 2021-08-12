from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.home, name='home'),
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