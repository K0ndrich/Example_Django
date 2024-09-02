# Файл хранит URL пути которые будут использоваться только для текущего приложения my_django_rest

# django
from django.urls import path, include

# my_project
from my_django_rest.views.views import WomenAPIView, WomenAPIList


urlpatterns = [
    #
    # вызов представления API без роутера
    path("my_api_view/", WomenAPIView.as_view()),
    #
    # представление предназначено только для вывода набора ячеек из базы
    path("my_api_list/", WomenAPIList.as_view()),
    #
    # внутрь url-адреса передаем переменную pk с типом данных int
    # изменяет уже существующие ячейки в базе или удаляем ети ячейки по id-ключу
    path(
        "my_api_view/<int:pk>/", WomenAPIView.as_view()
    ),  # -> 127.0.0.1:8000/my_api_view/1/
]
