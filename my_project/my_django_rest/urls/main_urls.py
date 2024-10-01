# Файл хранит URL пути которые будут использоваться только для текущего приложения my_django_rest

# django
from django.urls import path, include, re_path

# django_rest
from rest_framework.routers import SimpleRouter, DefaultRouter

# my_project
from my_django_rest.views.my_own_api_view import WomenAPIView
from my_django_rest.views.views import WomenAPIList, WomenAPIUpdate, WomenAPIDetailView
from my_django_rest.views.viewsets import WomenViewSet
from my_django_rest.views.permissions_views import (
    WomenAPIList,
    WomenAPIUpdate,
    WomenAPIDestroy,
)


# роутеры упрощают маршрутизацию(прописание url-адрессов) для django rest
# создание простого роутера
# my_router = SimpleRouter()

# DefaultRouter хранит внутри себя больше url-адрессов чем SimpleRouter
# также при написании основного url-адресса без продолжения, который указан в роутере не выдает ошибку, а возвращает сам url-адресс но с продолжением
# основной url-адресс без продолжения http://127.0.0.1:8000/my_router/
my_router = DefaultRouter()

# регистрация нового пути внутрь нашего роутера my_router
# r " " регулярное выражение, префикс для набора маршрутов , будет вставляться в конце каждого маршрута, где будем использовта
# basename указывает name для url-путей текущего роутера, также basename нужно указывать если не определен стандартный queryset
my_router.register(r"women", WomenViewSet, basename="women")

# возвращает все маршруты, которые храняться в указаном роутере my_router
my_router.urls

urlpatterns = [
    #
    # вызов представления API без роутера
    path("my_api_view/", WomenAPIView.as_view()),  # -> 127.0.0.1:8000/my_api_view/
    #
    # внутрь url-адреса передаем переменную pk с типом данных int
    # изменяет уже существующие ячейки в базе или удаляем ети ячейки по id-ключу
    path(
        "my_api_view/<int:pk>/", WomenAPIView.as_view()
    ),  # -> 127.0.0.1:8000/my_api_view/4/
    #
    # представление предназначено только для вывода набора ячеек из базы
    path("my_api_list/", WomenAPIList.as_view()),
    #
    # изменение одной записи по get- , put- запросам
    path("my_api_list/<int:pk>/", WomenAPIUpdate.as_view()),
    #
    # позволяет читать, изменять и удалять отдельные записи по get- , put- , patch- , delete- запросам
    path("my_api_detail/<int:pk>/", WomenAPIDetailView.as_view()),
    #
    path(
        "my_router/", include(my_router.urls)
    ),  # -> http://127.0.0.1:8000/my_router/women/
    # -> http://127.0.0.1:8000/my_router/women/<int:pk>/
    #
    # ВНУТРИ РОУТЕРА НАХОДИТЬСЯ ВСЕ ЧТО НИЖЕ
    # вызываеться не одно api-представление, а набор api-представлений
    # нужно указывать методы для каждого типа запросов, обрабатывает только указаный метод запроса
    #
    # { "тип_запроса" : "мой_метод_из_viewset" }
    # path("my_api_viewset/", WomenViewSet.as_view({"get": "list"})),
    #
    # вызывает другой метод (действие) в viewset
    # path("my_api_viewset/<int:pk>/", WomenViewSet.as_view({"put": "update"})),
    #
    #
    # ПРАВА ДОСТУПА ПОЛЬЗОВАТЕЛЕЙ (PERMISSIONS)
    path("women/", WomenAPIList.as_view()),
    path("women/<int:pk>/", WomenAPIUpdate.as_view()),
    path("womendelete/<int:pk>/", WomenAPIDestroy.as_view()),
]
