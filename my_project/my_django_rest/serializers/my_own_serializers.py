# СОЗДАЕМ СВОЙ СЕРИАЛИЗАТОР


# django

# django_rest
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

# my_project


# просто создает одну строку формата НЕ json
class WomenModel:
    def __init__(self, title, content):
        # создаем локальные атрибуты екзепляра класса, просто наша строка (пока НЕ json)
        self.title = title
        self.content = content


# проводит сериализацию строки, которую создаем в WomenModel
# текущий класс унаследуеться от базового класса сериализации Serializer
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


# функция преобразовывает простую строку в json-строку
def encode():

    model = WomenModel(title="Max_Kondrich", content="c-o-n-t-e-n-t")

    # переобразованые простой строки в словарь с данными
    model_sr = WomenSerializer(model)

    print(model_sr.data, type(model_sr.data), sep="\n")
    model_sr.data  # -> {'title': 'Max_Kondrich', 'content': 'c-o-n-t-e-n-t'}
    type(
        model_sr.data
    )  # -> <class 'rest_framework.utils.serializer_helpers.ReturnDict'>

    # преобразовывает сериализованую строку в json-строку
    json = JSONRenderer().render(model_sr.data)

    print(json, type(json), sep="\n")

    json  # -> b'{"title":"Max_Kondrich","content":"c-o-n-t-e-n-t"}'
    type(json)  # -> <class 'bytes'>
