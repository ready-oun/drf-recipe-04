from rest_framework import generics
from .models import Recipe
from .permissions import IsAuthenticatedOrReadOnly
from .serializers import RecipeSerializer

"""
IsAuthenticatedOrReadOnly 권한 클래스 사용해서
비로그인 유저는 GET 요청만 가능(읽기 전용),
로그인 유저는 GET 포함 POST, PUT, PATCH, DELETE 요청 가능
"""


class RecipeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class RecipeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
