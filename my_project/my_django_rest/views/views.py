# Файл содежит только API-Предствления для django_rest
# API-Представление хранят в себе возможность пользователя взаемодействовать с всеми типами запросов (get- , post-, put-, patch-, delete-)


# django
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response

# django_rest
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView


# my_project
from my_django_rest.models import Women
from my_django_rest.serializers.main_serializers import WomenSerializer


# ListCreateAPIView предназначен для вывода набора записей базы данных по get-запросу и добавление новый записей по post-запросу
class WomenAPIList(ListCreateAPIView):
    # queryset указывает какие записи из базы будем выводить
    queryset = Women.objects.all()
    # serializer_class указывает каким сериализатором будем пользоваться
    serializer_class = WomenSerializer


# придназначен для изменения записи по put- , patch- запросам
# клиенту будет возвращаться только одна измененая запись
class WomenAPIUpdate(UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# RetrieveUpdateDestroyAPIView добавляет возможность чтения , изменения и удаление отдельной записи
# по get- , put- , patch- , delete- запросам
class WomenAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
