from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['food_type_id', 'food_ingredients_id', 'title', 'content', 'thumbnail', 'difficulty']
        """
        'user_id'는 요청을 보내는 유저로부터 자동으로 설정된다? 그래서 필드에 포함 안 함 
        모두 포함하려면 위 삭제하고 아래 주석 풀어서 ㄱㄱ
        """
        # fields = '__all__'

    def create(self, validated_data):
        recipe = Recipe.objects.create(**validated_data)
        return recipe
