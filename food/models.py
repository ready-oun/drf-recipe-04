from django.db import models


class FoodType(models.Model):
    food_type_image = models.URLField(max_length=200, null=False)  # 이미지 URL 필드
    food_type_name = models.CharField(max_length=100, null=False)  # 음식 종류 이름 필드
    # created_at = models.DateTimeField(auto_now_add=True)  # 생성일자, 자동으로 현재 시간 저장
    # updated_at = models.DateTimeField(auto_now=True)  # 수정일자, 자동으로 현재 시간 저장

    def __str__(self):
        return self.food_type_name  # 객체를 문자열로 표현할 때 음식 종류 이름을 반환


class FoodIngredient(models.Model):
    food_ingredient_image = models.URLField(max_length=200, null=False)  # 이미지 URL 필드
    food_ingredient_name = models.CharField(max_length=100, null=False)  # 음식 재료 이름 필드
    # created_at = models.DateTimeField(auto_now_add=True)  # 생성일자, 자동으로 현재 시간 저장
    # updated_at = models.DateTimeField(auto_now=True)  # 수정일자, 자동으로 현재 시간 저장

    def __str__(self):
        return self.food_ingredient_name  # 객체를 문자열로 표현할 때 음식 재료 이름을 반환
