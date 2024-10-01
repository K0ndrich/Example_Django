# Файл хранит кастомные классы права доступа пользователей Permission

# django_rest
from rest_framework.permissions import BasePermission
from rest_framework import permissions


# создание класса, который хранит права доступа для пользователей
# администартора имеет все права доступа, а другие пользователи могут только читать данные ячеек
class IsAdminOrReadOnly(BasePermission):

    # хранит органичение прав доступа на уровне всего api-представления
    def has_permission(self, request, view):

        # permissions.SAFE_METHODS хранит url-запросы только для чтения данных
        if request.method in permissions.SAFE_METHODS:

            # return True права доступа предоставлены пользователю
            # return False права доступа НЕ предоставлены пользователю
            return True

        # проверяем являеться ли пользователь админитсратором
        return bool(request.user and request.user.is_staff)


# создателья ячейки данных имеет все права доступа, а все остальные пользователи(включая админитсратора) могуть только читать
class IsOwnerOrReadOnly(permissions.BasePermission):
    # хранит органичение прав доступа на уровне одной отдельной текущей ячейкой
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # имя пользователя который создал == имя пользователя который отправил запрос на сервер
        return obj.user == request.user
