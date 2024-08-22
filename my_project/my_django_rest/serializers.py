# Файл создержит сериализаторы для нашего API

# django_rest
from rest_framework.serializers import ModelSerializer

# my_project
from my_django_rest.models import Women


class WomenSerializer(ModelSerializer):

    class Meta:
        # model указывает с какой моделью django будет работать текущий сериализатор
        model = Women
        # fields указывает поля модели, которые будут отправляться пользователю назад
        # fields = "__all__"  указываем все поля
        # cat_id ето значение колонки из модели на которую мы ссылаемся
        fields = ("title", "cat_id")
