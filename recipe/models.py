from django.db import models
from user.models import CustomUser
# from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from food.models import FoodType, FoodIngredient


class Recipe(models.Model):
    """
    pk 자동 생성, DateTimeFields 는 common Model 에서 가져옴.
    FoodType, FoodIngredient 는 Food app 에 있는 것으로 가정함.
    Favorite 은 Favorite app 을 따로 생성한 것으로 가정함.
    """
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    food_type_id = models.ForeignKey(FoodType, on_delete=models.CASCADE, null=False)
    food_ingredient_id = models.ManyToManyField(FoodIngredient)  # 여러 개 생성 위해 MToM
    title = models.CharField(max_length=255, null=False)
    content = RichTextField(null=False)  # django-ckeditor 패키지의 커스텀 필드라서 models. 없이 작성해야 정상적으로 import함.
    thumbnail = models.ImageField(null=True, blank=True, upload_to='recipe/thumbnail')  # S3 설정 완료 후에 링크삽입
    difficulty = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title
