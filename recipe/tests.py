from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Recipe
from food.models import FoodType, FoodIngredient
from user.models import CustomUser

User = get_user_model()

"""
API Test를 위하여 두 테스트 유저를 생성해
1. 레시피 리스트 조회
2. 레시피 생성
3. 레시피 상세 조회 및 수정(비인증)
4. 레시피 삭제(소유자)
5. 레시피 수정(비소유자)
위 케이스를 테스트합니다. 
"""


class RecipeTests(APITestCase):
    def setUp(self):
        # Generate 2 Test Users
        self.user = CustomUser.objects.create_user(email='testuser@gmail.com', name='Readya Tester', password='testpassword')
        self.user2 = CustomUser.objects.create_user(email='testuser2@kakao.com', name='Rhoarbinne Hoot', password='test2password')
        self.client = APIClient()
        self.food_type = FoodType.objects.create(food_type_name='국/찌개')
        self.food_ingredient = FoodIngredient.objects.create(food_ingredient_name='닭고기')
        self.recipe = Recipe.objects.create(
            user=self.user,
            food_type=self.food_type,
            food_ingredient=self.food_ingredient,
            title='Test Recipe',
            content='Test Recipe Content',
            difficulty='Newbie'
        )
        self.recipe.food_ingredient.add(self.food_ingredient)

    def test_get_recipe_list(self):
        # 1. 리스트 조회 : 비로그인 상태에서도 레시피 리스트 조회 가능
        url = reverse('recipe-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_recipe_authentication(self):
        # 2. 게시글 생성 : 로그인 유저만 레시피 생성 가능
        self.client.login(username='testuser', password='testpassword')
        url = reverse('recipe-list-create')
        data = {
            # 'user': self.user, # view에서 현재 로그인한 사용자를 자동으로 할당 - 요청 데이터에 포함X
            'food_type': self.food_type.pk,
            'title': 'New Recipe',
            'content': 'New Recipe Content',
            'difficulty': 'Gosu',
            'food_ingredients': [self.food_ingredient.pk]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_recipe_detail_unauthenticated(self):
        # 3. 상세 조회 및 수정(비인증): 비로그인 유저는 레시피 수정 불가한지 시도
        url = reverse('recipe-detail', args=[self.recipe.id])
        data = {'title': 'Recipe to Update'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_recipe_delete_owner(self):
        # 4. 삭제: 게시글 소유자가 레시피 삭제
        self.client.login(username='testuser', password='testpassword')
        url = reverse('recipe-detail', args=[self.recipe.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_recipe_update_not_owner(self):
        # 5. 수정: 레시피 게시글을 작성하지 않은 사람이 레시피를 수정할 수 없음
        self.client.login(username='testuser2', password='test2password')
        url = reverse('recipe-detail', args=[self.recipe.id])
        data = {'title': 'Updated Recipe Title'}
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

