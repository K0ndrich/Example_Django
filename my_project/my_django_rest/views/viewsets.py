# Viewsets ето наборы API-Предствалений
# Viewsets дают возможность пользователю взаемодействовать не с типами запросом, а с целыми методами действий с базой данных
# Viewsets обединяет все типы запросов внутри себя и дает методы(действия) над етими запросами

# django_rest
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

# my_project
from my_django_rest.models import Women
from my_django_rest.serializers.main_serializers import WomenSerializer


# # ModelViewSet набор представлений для работы с моделью (по-простому)
class WomenViewSet(ModelViewSet):

    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# набор представлений для работы с моделью (по-сложному) , тоже самое что и сверху
# class WomenViewSet(
#     # mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.ListModelMixin,
#     GenericViewSet,
# ):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# ReadOnlyModelViewSet предназначен для взаемойдествия с нащшей таблицей только через get-запросы
# class WomenReadOnlyViewSet(ReadOnlyModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
