# Файл хранит URL пути которые будут использоваться только для текущего приложения my_django

# django
from django.urls import path, include

# my_project
from my_django.views.main_views import my_view, MyView
from my_django.views.request_views import my_request_data

urlpatterns = [
    # вызов представления основанное на функции
    # name указывает как монжно обращаться  етому пути в html коде
    # <a href="{% url 'my_function_view' %}" </a>
    path("my_function_view/", my_view, name="my_function_view"),
    # 
    # <a href="{% url 'my_detail_function_view' id %}" </a>
    path("my_function_view/<int:id>", my_view, name="my_detail_function_view"),
    # 
    # вызов представлениея основанное на классе
    path("my_classes_view/", MyView.as_view()),
    # 
    # разбираем наш request из чего состоит
    path("my_request_data/", my_request_data),
    #
]
