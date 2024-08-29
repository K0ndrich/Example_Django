# Файл хранит URL пути которые будут использоваться только для текущего приложения my_django

# django
from django.urls import path, include

# my_project
from my_django.views.main_views import my_view, MyView
from my_django.views.request_views import my_request_data

urlpatterns = [
    # name позволяет обращаться к етому url-адресу в коде
    # вызов представлениея основанное на функции
    path("my_function_view/", my_view),
    # вызов представлениея основанное на классе
    path("my_classes_view/", MyView.as_view()),
    # разбираем наш request из чего состоит
    path("my_request_data/", my_request_data),
    #
]
