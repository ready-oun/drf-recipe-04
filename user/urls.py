from django.urls import path
from .views import CustomUserCreate, CustomUserList

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name='create_user'),
    path('list/', CustomUserList.as_view(), name='list_user'),
]
