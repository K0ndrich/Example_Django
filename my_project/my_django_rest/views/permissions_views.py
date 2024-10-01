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


# возвращает список ячеек
class WomenAPIList(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes хранит внутри себя указаные типы ограничения доступа для текущего api-представления
    permission_classes = (IsAuthenticatedOrReadOnly,)


# изменяет одну ячейку
class WomenAPIUpdate(RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # доступ к текущему api-представлению имеют только аутентифицырование пользователи
    permission_classes = (IsAuthenticated,)
    # пользователи получают доступ к текущему api-представлению только те кто аутентифицировался по токенам
    # по session_id аутентификации пользователь получить доступ к api-представлению не может
    authentication_classes = (TokenAuthentication,)


# удаляет одну ячейку
class WomenAPIDestroy(RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # разрешение доступа для текущего api-представления только для админа
    permission_classes = (IsAdminOrReadOnly,)
