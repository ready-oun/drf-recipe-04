from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer

"""
이 예시에서는 간단히 모든 사용자에게 접근 권한을 부여하였지만, 
실제 애플리케이션에서는 보안과 권한 관리를 위해 이를 조정할 필요가 있습니다.
"""

class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # 이 예제에서는 누구나 사용자를 생성할 수 있도록 설정합니다.
    permission_classes = [permissions.AllowAny]

class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # 이 예제에서는 누구나 사용자 목록을 볼 수 있도록 설정합니다.
    permission_classes = [permissions.AllowAny]
