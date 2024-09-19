# Viewsets ето наборы API-Предствалений
# Viewsets дают возможность пользователю взаемодействовать не с типами запросом, а с целыми методами действий с базой данных
# Viewsets обединяет все типы запросов внутри себя и дает методы(действия) над етими запросами

# django_rest
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response


# my_project
from my_django_rest.models import Women, Category
from my_django_rest.serializers.main_serializers import WomenSerializer




# # ModelViewSet набор представлений для работы с моделью (по-простому)
class WomenViewSet(ModelViewSet):

    # queryset опередлен ниже
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    # функция get_queryset дает возможность переопредилить выполнение queryset
    def get_queryset(self):

        # бер значение pk от пользователя в url-адресе
        pk = self.kwargs.get("pk")

        # если пользователь не указал pk одной конкретной записи
        if not pk:
            # берем только три первые записи с помощью срезов
            return Women.objects.all()[:3]

        # если пользователь указал pk одной конкретной записи, тогда возвращаем ету запись, но в виде списка
        # берем filter потому что он возвращает списко даже с одной записью, queryset принимает только список
        return Women.objects.filter(pk=pk)

    # action позволяет добавлять свои url-адресса с функционалом, который еще не продуман
    # methods указывает какие методы запросов будет поддерживать наш новый url-путь
    # detail=False указывает, что будем возвращать список записей, а не только одну запись
    @action(methods=["get"], detail=False)
    def category(self, request):  # -> http://127.0.0.1:8000/my_router/women/category/
        # берем все ячейки со всеми характеристиками из модели Category
        cats = Category.objects.all()
        return Response({"cats": [c.name for c in cats]})

    # url-адресс для вывода только одного значения по pk из модели Category
    @action(methods=["get"], detail=True)
    def one_category(
        self, request, pk=None
    ):  # -> http://127.0.0.1:8000/my_router/women/1/one_category/
        # берем все ячейки со всеми характеристиками из модели Category
        cat = Category.objects.get(pk=pk)
        return Response({"cats": cat.name})


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
