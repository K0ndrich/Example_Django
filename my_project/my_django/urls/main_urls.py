# Файл хранит URL пути которые будут использоваться только для текущего приложения my_django

# django
from django.urls import path, include, re_path

# my_project
from my_django.views.main_views import my_view, MyView, my_expression
from my_django.views.request_views import my_request_data

# указывает название пространства имен namespace для текущего приложения для url-путей внутри html кода
app_name = "my_django"

# https:  //127.0.0.1  :8000  /my_view/
# https       - указаные протокола, которым будем пользоваться для передачи данных
# 127.0.0.1   - ip-адресс(также домен) на котром будет работаь наш проект
# 8000        - порт по которому общаемся с пользователем, слушам 8000 порт ето принимаем данные по 8000 порту от пользователя
# /my_view/   - название простого представления (или api-представления), которое реализовано внутри проекта

urlpatterns = [
    # вызов представления основанное на функции
    # name указывает как можно обращаться  етому пути в html коде
    # <a href="{% url 'my_django:my_function_view' %}" </a>
    # my_django указывает пространство имент текущего url-пути, указывает из какого приложения будем брать name url-пути в html коде
    path("my_function_view/", my_view, name="my_function_view"),
    #
    # <int:id> указывает что можем передавать значение прямо в url-адресс, значение должно быть указаного типа int
    # <a href="{% url 'my_django:my_detail_function_view' item.id %}" </a>
    path("my_function_view/<int:id>/", my_view, name="my_detail_function_view"),  # ->
    # -> http://127.0.0.1:8000/my_function_view/7/
    #
    # вызов представлениея основанное на классе 
    path("my_classes_view/", MyView.as_view()),
    #
    # разбираем наш request из чего состоит
    path("my_request_data/", my_request_data),
    #
    # re_path позволяет использовать регулярные выражения внутри url-адресса
    # в текущем случаем главное чтоб url-адресс начинался с my_expression, не важно как будет заканчиваться
    re_path(r"^my_expression", my_expression),  # ->
    # -> http://127.0.0.1:8000/my_expression/
    # -> http://127.0.0.1:8000/my_expression_name/
    # -> http://127.0.0.1:8000/my_expression/about/
    # -> http://127.0.0.1:8000/my_expression/777/
    # 
]
