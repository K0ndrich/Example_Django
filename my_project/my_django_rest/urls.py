# Файл хранит URL пути которые будут использоваться только для текущего приложения my_django_rest

# django
from django.urls import path, include

# my_project
from my_django.views import my_view2

urlpatterns = [
    path("my_view2/", my_view2),
]
