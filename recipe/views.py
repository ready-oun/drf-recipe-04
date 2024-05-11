from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Recipe
from .serializers import RecipeSerializer


class CreateRecipeAPIView(generics.GenericAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]  # 여러 개 권한 클래스를 리스트로 받아서 인증된 사용자만 접근 가능

    def post(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)

        # data validity
        if not serializer.is_valid():
            return Response({'error': 'Not Valid Data', 'details': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save(user=user)
        return Response({'success': 'Recipe Successfully Created', 'data': serializer.data},
                        status=status.HTTP_201_CREATED)


# post: genericAPIView 말고 List~ 알아보고 수정
class ListRecipeAPIView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Recipe.objects.filter(

        )