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

        my_list = Women.objects.all().values()

        return Response({"womens": list(my_list)})
        # возвращает ответ в типе django_rest
        # return Response({"my_get_request": "Kondrich"})

    # метод обрабатывает post-запросы от пользователя к сайту, добавление ячеек в модель(базу данных)
    def post(self, request):
        post_new = Women.objects.create(
            # request.data["title"] ето значения которие мы прописываев в url-адресе при post-запросе
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"],
        )
        # model_to_dict преобразовывает йчейку из модели и словарь
        return Response(
            {"post": model_to_dict(post_new)}
        )  # -> {"post":{"id":5,"title":"Oleksey","content":"My_Content7","is_published":true,"cat":2}}


# ListAPIView предназначен для вывода списока обьектов через api
# class WomenAPIView(ListAPIView):
#     # queryset указывает какие обьекты будем выводить
#     queryset = Women.objects.all()
#     # serializer_class указывает каким сериализатором будем пользоваться
#     serializer_class = WomenSerializer
