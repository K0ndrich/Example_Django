# Ограничения Доступа - Permissions


# django_rest
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# my_project
from my_django_rest.models import Women, Category
from my_django_rest.serializers.main_serializers import WomenSerializer
from my_django_rest.custom_permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


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
    permission_classes = (IsOwnerOrReadOnly,)


# удаляет одну ячейку
class WomenAPIDestroy(RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # разрешение доступа для текущего api-представления только для админа
    permission_classes = (IsAdminOrReadOnly,)
