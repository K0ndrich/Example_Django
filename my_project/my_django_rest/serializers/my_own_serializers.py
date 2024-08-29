# СОЗДАЕМ СВОЙ СЕРИАЛИЗАТОР


# django

# django_rest
import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# my_project


# просто создает одну строку формата НЕ json
class WomenModel:
    def __init__(self, title, content):

        # создаем локальные атрибуты екзепляра класса, просто наша строка (пока НЕ json)
        self.title = title
        self.content = content


# -----   СВОЙ СОЗДАНЫЙ СЕРИАЛИЗАТОР С НУЛЯ   --------------------------------------------------------------------------------------------------------------------------------------------


# текущий класс унаследуеться от базового класса сериализации Serializer
class WomenSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    # read_only=True поле используеться только для чтения
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    # добавление новой записи в базу данных (сохраняет их в базе)
    # validated_data хранит словарь наших данных, которые мы передавали в url-адресс
    def create(self, validated_data):

        # **validated_data розпаковываем словрь с данными
        return Women.objects.create(**validated_data)

    # изменение уже существующей записи в базе данных (перезаписывает ее в базе)
    def update(self, instance, validated_data):

        # берез значение из словаря validated_data по указаному ключю
        # если значение не находим, тогда возвращаем значение по умолчанию instance.title
        instance.title = validated_data.get("title", instance.title)

        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("time_update", instance.is_published)
        instance.cat_id = validated_data.get("time_update", instance.cat_id)

        # перезаписывает запись в базе
        instance.save()


# -----   ОТДЕЛЬНЫЕ ФУНКЦИИ   --------------------------------------------------------------------------------------------------------------------------------------------


# encode функция преобразовывает простой словарь в json-строку
def encode():

    model = WomenModel(title="Max_Kondrich", content="c-o-n-t-e-n-t")

    # переобразованые простой строки в словарь с данными
    model_sr = WomenSerializer(model)

    model_sr.data  # -> {'title': 'Max_Kondrich', 'content': 'c-o-n-t-e-n-t'}
    type(
        model_sr.data
    )  # -> <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

    # преобразовывает наш словарь в json-строку
    json = JSONRenderer().render(model_sr.data)

    json  # -> b'{"title":"Max_Kondrich","content":"c-o-n-t-e-n-t"}'
    type(json)  # -> <class 'bytes'>


# функция преобразовывает json-строку в словарь
def decode():
    # содержит json-строку
    stream = io.BytesIO(b'{"title":"Max_Kondrich","content":"c-o-n-t-e-n-t"}')

    stream  # -> <_io.BytesIO object at 0x000001B4F29D8400>
    type(stream)  # -><class '_io.BytesIO'>

    data = JSONParser().parse(stream)

    data  # -> {'title': 'Max_Kondrich', 'content': 'c-o-n-t-e-n-t'}
    type(data)  # -> <class 'dict'>

    # переводим json-строку в словарь
    serializer = WomenSerializer(data=data)

    # проверка десериализовных данных на верность
    serializer.is_valid()

    serializer.validated_data  # -> {'title': 'Max_Kondrich', 'content': 'c-o-n-t-e-n-t'}
    type(serializer.validated_data)  # -> <class 'dict'>
