# Файл хранит URL пути по которым вызываються представления из views.py или подключаються другие пути urls.py


"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django
from django.contrib import admin
from django.urls import path, include

# django_rest
from rest_framework.routers import SimpleRouter

# my_project
from my_django.views.main_views import my_view, MyView, my_request_data
from my_django_rest.views.views import WomenAPIView


# создание роутера django_rest
# router = SimpleRouter()

# регистрация нового пути для нашего текущего роутера django_rest
# router.register(
#     "api/my_api_view", MyAPIView
# )  # -> http://127.0.0.1:8000/api/my_api_view


urlpatterns = [
    # path("url-путь/", view-представление, name="название_пути для обращения в index.html"),
    #
    # путь попадения в панель администратора
    path("admin/", admin.site.urls),
    # вызов представлениея основанное на функции
    path("my_function_view/", my_view),
    # вызов представлениея основанное на классе
    path("my_classes_view/", MyView.as_view()),
    # вызов представления API без роутера
    path("my_api_view/", WomenAPIView.as_view()),
    # разбираем наш request из чего состоит
    path("my_request_data/", my_request_data),
    # подключаем файлы с url-путями наших приложений my_django, my_django_rest  к проекту
    path("", include("my_django.urls")),
    path("", include("my_django_rest.urls")),
]


# добавление всех путей из роутера django_rest к глобальным url путям нашего проекта
# urlpatterns += router.urls
