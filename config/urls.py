from django.contrib import admin
from django.urls import path, include
import base.urls, user.urls, post.urls, signup.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base.urls)),
    path('user/', include(user.urls)),
    path('post/', include(user.urls)),
    path('signup/', include('signup.urls')),        # 회원가입 url 수정 - 래현
]

