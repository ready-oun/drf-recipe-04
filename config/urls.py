from django.contrib import admin
from django.urls import path, include
# from user.views import CustomUserCreate, CustomUserList

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('recipe.urls')),
    # path('user/', include('user.urls')),
    # path('', include('common.urls')),
]
# # 미디어 파일에 대한 URL 패턴 추가
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
