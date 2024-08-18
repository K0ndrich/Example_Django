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

# my_project
from my_app.views import my_view


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