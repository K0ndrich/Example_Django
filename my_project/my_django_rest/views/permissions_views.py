# Ограничения Доступа - Permissions


# django_rest
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication

# my_project
from my_django_rest.models import Women, Category
from my_django_rest.serializers.main_serializers import WomenSerializer
from my_django_rest.permissions.custom_permissions import (
    IsAdminOrReadOnly,
    IsOwnerOrReadOnly,
)


# AllowAny - полный доступ
# IsAuthenticated - только для авторизированых пользователей
# IsAdminUser - только для администраторов
# IsAuthenticatedOrReadOnly - только для авторизованым или всем, но только для чтения


# ПОЛЬЗОВАТЕЛЬСИЙ КЛАСС ПАГИНАЦИИ между страницами ячеек django_rest
class WomenAPIListPagination(PageNumberPagination):
    # хранит количество записей на странице по-умолчанию
    page_size = 3
    # page_size ето название дополнительного параметра в get-запросе для изменения значения page_size
    # -> http://127.0.0.1:8000/my_api_list/?limit=10&offset=4&page_size=7
    page_size_query_param = "page_size"
    # хранит максимальное значение page_size (page_size_query_param), которое может ввести пользователь в get-запросе к сайту
    max_page_size = 20


# возвращает список ячеек
class WomenAPIList(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes хранит внутри себя указаные типы ограничения доступа для текущего api-представления
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # указываем класс пагинации для страниц с ячейками django_rest, работает только для одного текущего api-представления
    pagination_class = WomenAPIListPagination


# изменяет одну ячейку
class WomenAPIUpdate(RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # доступ к текущему api-представлению имеют только аутентифицырование пользователи
    permission_classes = (IsAuthenticated,)
    # ПОДКЛЮЧЕНИЕ DJOISER TOKEN
    # пользователи получают доступ к текущему api-представлению только те кто аутентифицировался по токенам
    # по session_id аутентификации пользователь получить доступ к api-представлению не может
    # authentication_classes = (TokenAuthentication,)


# удаляет одну ячейку
class WomenAPIDestroy(RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # разрешение доступа для текущего api-представления только для админа
    permission_classes = (IsAdminOrReadOnly,)
