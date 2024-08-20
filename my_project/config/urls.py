# Файл хранит URL пути по которым вызываються представления из views.py


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
from my_app.views import my_view, MyAPIView


# создание роутера django_rest
router = SimpleRouter()

# регистрация нового пути для нашего текущего роутера django_rest
router.register(
    "api/my_api_view", MyAPIView
)  # -> http://127.0.0.1:8000/api/my_api_view


urlpatterns = [
    # path("url-путь/", view-представление, name="название_пути для обращения в index.html"),
    #
    # путь попадения в панель администратора
    path("admin/", admin.site.urls),
    # путь в попадение в одно представление
    path("my_view/", my_view),
    # подключаем пути только для одного отдельного приложения my_app
    path("", include("my_app.urls")),
]


# добавление всех путей из роутера django_rest к глобальным url путям нашего проекта
urlpatterns += router.urls
