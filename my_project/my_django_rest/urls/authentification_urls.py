# Файл хранит пути для Аунтентификации и Авторизации пользователей разными способами

# django
from django.urls import path, include, re_path


urlpatterns = [
    # 1) АУТЕНТИФИКАЦИЯ ПОЛЬЗОВАТЕЛЕЙ (Session-Based Authentification) встроеная в django_rest
    path(
        "auth/", include("rest_framework.urls")
    ),  # -> http://127.0.0.1:8000/auth/login/
    # -> http://127.0.0.1:8000/auth/logout/
    #
    #
    # 2) АУТЕНТИФИКАЦИЯ ПОЛЬЗОВАТЕЛЕЙ ПО ТОКЕНАМ DJOISER (Token-Based Authentificatiion)
    # пути для djoiser смотрим в https://djoser.readthedocs.io/en/latest/base_endpoints.html
    path("auth/", include("djoser.urls")),
    # -> http://127.0.0.1:8000/auth/users/
    #
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    # -> http://127.0.0.1:8000/auth/token/login/   создание токена аутентификации для пользователя
    # -> http://127.0.0.1:8000/auth/token/logout/   удаление токена аутентификации для пользователя
]
