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

# my_project
from my_django.views.main_views import my_view, MyView
from my_django.views.request_views import my_request_data
from my_django_rest.views.my_own_api_view import WomenAPIView


urlpatterns = [
    # path("url-путь/", view-представление, name="название_пути для обращения в index.html"),
    #
    # путь попадения в панель администратора
    path("admin/", admin.site.urls),
    #
    # подключаем файлы с url-путями наших приложений my_django, my_django_rest  к проекту
    # namespace указывает пространство имен для одного приложени
    # namespace нужен во избежание путаници с одиниковыми name разных приложений
    path("", include("my_django.urls", namespace="my_django")),
    path("", include("my_django_rest.urls")),
]


# добавление всех путей из роутера django_rest к глобальным url путям нашего проекта
# urlpatterns += router.urls
