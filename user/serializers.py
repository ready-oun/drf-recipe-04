from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'name', 'nickname', 'profile_image', 'is_social', 'is_active', 'is_staff', 'is_superuser', 'created_at', 'updated_at']
        # 비밀번호는 읽기 전용으로 설정하여 반환되지 않도록 합니다.
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # CustomUserManager의 create_user 메서드를 사용하여 비밀번호 해싱이 포함된 사용자 생성
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name']
        )
        return user
