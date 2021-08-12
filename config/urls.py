from django.contrib import admin
from django.urls import path, include
import base.urls, user.urls, post.urls, signup.urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base.urls)),
    path('user/', include(user.urls)),
    path('post/', include(post.urls)), #user쪽과 계속 겹쳐서 에러 발생하여 수정
    path('signup/', include('signup.urls')),        # 회원가입 url 수정 - 래현
]
if settings.DEBUG is True:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

