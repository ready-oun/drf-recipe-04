from rest_framework import generics, status
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'message': 'Recipe successfully created!',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)


class RecipeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
