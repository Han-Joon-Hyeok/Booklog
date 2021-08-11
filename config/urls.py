from django.contrib import admin
from django.urls import path, include
import base.urls, user.urls, post.urls, signup.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base.urls)),
    path('user/', include(user.urls)),
    path('post/', include(post.urls)), #user쪽과 계속 겹쳐서 에러 발생하여 수정
    path('signup/', include('signup.urls')),        # 회원가입 url 수정 - 래현
]

