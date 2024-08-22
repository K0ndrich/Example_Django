# Файл хранит Сериализаторы для API предаствалений django_rest


# django

# django_rest
from rest_framework.serializers import ModelSerializer

# my_project
from my_django.models import MyModel1


class OrderSerializer(ModelSerializer):

    class Meta:
        # указываем с какой моделью(таблицей базы данных) будем работать
        model = MyModel1
        # указываем поля(колоник) текущей модели значения которых будем возвращать
        #  fields = '__all__' указываем что будем взаемодействовать со всеми колонками таблици
        fields = ["my_column1", "my_column2"]
