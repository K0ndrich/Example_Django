# Файл содежит только API-VIEWS для django_rest

# django
from django.shortcuts import render

# django_rest
from rest_framework.generics import ListAPIView

# my_project
from my_django_rest.models import Women
from my_django_rest.serializers import WomenSerializer


# ListAPIView предназначен для вывода списока обьектов
class WomenAPIView(ListAPIView):
    # queryset указывает какие обьекты будем выводить
    queryset = Women.objects.all()
    # serializer_class указывает каким сериализатором будем пользоваться
    serializer_class = WomenSerializer
