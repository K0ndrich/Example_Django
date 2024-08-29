# Файл содежит только API-VIEWS для django_rest

# django
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response

# django_rest
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

# my_project
from my_django_rest.models import Women
from my_django_rest.serializers.main_serializers import WomenSerializer


# APIView унаследуемся от базового класса, стоит во главе иерархии
class WomenAPIView(APIView):

    # метод обрабатыает get-запросы от пользователя к сайту
    def get(self, request):

        my_objects = Women.objects.all()

        # 1) ВАРИАНТ
        # many=True указываем что сериализатору нужно оборабатывать не одну запись, а набор записей
        return Response(
            {"posts": WomenSerializer(my_objects, many=True).data}
        )  # -> {"posts":[{"title":"Women_1","cat_id":1},{"title":"Women_2","cat_id":2},{"title":"Women_3","cat_id":1},{"title":"Women_4","cat_id":1},{"title":"Oleksey","cat_id":2},{"title":"my_name","cat_id":2}]}

        # 2) ВАРИАНТ
        # возвращает ответ в типе django_rest
        # return Response({"my_get_request": "Kondrich"})

    # метод обрабатывает post-запросы от пользователя к сайту, только отправляет данные на сервер (не сохраняет их там)
    def post(self, request):

        # розпоковываем json строку полученую из url-адресса в список словарей
        serializer = WomenSerializer(data=request.data)
        # проверка на уровне сериализатора правильно ли указаны все параметры в url-адресе
        # ловим ошибку, которая вылетит
        serializer.is_valid(
            raise_exception=True
        )  # -> "title": ["Ето поле обязательное"]

        # 1) ВАРИАНТ С МЕТОДОМ CREATE СЕРИАЛИЗАТОРА
        # добавление текущей новой ячейки в базу данных
        # вызов сериализаторе нашего метода create
        serializer.save()

        # 2) ВАРИАНТ БЕЗ МЕТОДА СЕРИАЛИЗАТОРА
        # post_new = Women.objects.create(
        #     # request.data["title"] ето значения которие мы прописываев в url-адресе при post-запросе
        #     title=request.data["title"],
        #     content=request.data["content"],
        #     cat_id=request.data["cat_id"],
        # )

        return Response(
            {"posts": serializer.data}
        )  # -> {"posts":{"title":"my_name","cat_id":2}}

    # перезаписывает запись в базе данных
    # вызывает метод update из нашего сериализатора
    def put(self, request, *args, **kwargs):

        pk = kwargs.get("pk", None)


# ListAPIView предназначен для вывода списока обьектов через api
# class WomenAPIView(ListAPIView):
#     # queryset указывает какие обьекты будем выводить
#     queryset = Women.objects.all()
#     # serializer_class указывает каким сериализатором будем пользоваться
#     serializer_class = WomenSerializer
