# Файл хранит пути для Аунтентификации и Авторизации пользователей разными способами

# django
from django.urls import path, include, re_path

# django_rest

# django_rest_simple_jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # 1) АУТЕНТИФИКАЦИЯ ПОЛЬЗОВАТЕЛЕЙ ПО СЕССИЯМ (Session-Based Authentification) встроеная в django_rest
    path("auth/", include("rest_framework.urls")),  # ->
    # -> http://127.0.0.1:8000/auth/login/
    # -> http://127.0.0.1:8000/auth/logout/
    #
    #
    # 2) АУТЕНТИФИКАЦИЯ ПОЛЬЗОВАТЕЛЕЙ ПО ТОКЕНАМ DJOISER (Token-Based Authentificatiion)
    # пути для djoiser смотрим в https://djoser.readthedocs.io/en/latest/base_endpoints.html
    path("auth/", include("djoser.urls")),  # ->
    # -> http://127.0.0.1:8000/auth/users/
    #
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    # -> http://127.0.0.1:8000/auth/token/login/   создание токена аутентификации для пользователя
    # -> http://127.0.0.1:8000/auth/token/logout/   удаление токена аутентификации для пользователя
    #
    #
    # 3) АУТЕНТИФИКАЦИЯ ПОЛЬЗОВАТЕЛЕЙ ПО JWT-ТОКЕНАМ SIMPLE JWT (Token-Based Authentificatiion)
    # получение access_token и refresh_token
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # ->
    # -> http://127.0.0.1:8000/api/token/
    #
    # выдача ного access_token при ввождении старого значения refresh_token
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # ->
    # -> http://127.0.0.1:8000/api/token/refresh/
    #
    # проверка access_token и refresh_token на правильность и действительность при ввождении их значений
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),  # ->
    # http://127.0.0.1:8000/api/token/verify/
]
