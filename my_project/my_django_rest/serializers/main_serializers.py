# Файл создержит сериализаторы для нашего API

# django_rest
from rest_framework import serializers



# my_project
from my_django_rest.models import Women


# сериализатор для взаемодейтсвия с моделью django
class WomenSerializer(serializers.ModelSerializer):

    class Meta:
        # model указывает с какой моделью django будет работать текущий сериализатор
        model = Women
        # fields указывает поля модели, которые будут отправляться пользователю назад
        # fields = "__all__"  указываем все поля
        # cat_id колонка cat из первой таблици, а id ето колонка из второй таблици
        fields = ("title", "cat_id")
