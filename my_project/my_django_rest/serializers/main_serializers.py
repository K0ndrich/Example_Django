# Файл создержит сериализаторы для нашего API

# django_rest
from rest_framework import serializers


# my_project
from my_django_rest.models import Women


# ModelSerializer сериализатор для взаемодейтсвия с модельями django
class WomenSerializer(serializers.ModelSerializer):

    # значения поля user из подели Women для ячейки береться из названия пользователя, который создат ету текущую ячейку
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        # model указывает с какой моделью django будет работать текущий сериализатор
        model = Women
        # fields указывает поля модели, которые будут отправляться пользователю назад
        # fields = ("title", "content", "cat")
        # указываем все поля
        fields = "__all__"
