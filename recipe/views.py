from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
# from .permissions import IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

"""
IsAuthenticatedOrReadOnly 권한 클래스 사용해서
비로그인 유저는 GET 요청만 가능(읽기 전용),
로그인 유저는 GET 포함 POST, PUT, PATCH, DELETE 요청 가능
    단, 게시물 수정, 삭제 요청 시 해당 게시글 작성자id가 같은지
    IsOwnerOrReadOnly 통해 권한 확인
"""


class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # post 요청한 유저를 게시물 작성자로 지정
        serializer.save(user_id=self.request.user)


class RecipeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [AllowAny]

    def get_object(self):
        # 요청 객체가 존재하지 않으면 404 반환
        obj = get_object_or_404(self.get_queryset(), id=self.kwargs('pk'))  # None 반환 위해 ['pk'] 대신 ('pk') 사용
        self.check_object_permissions(self.request, obj)
        return obj
