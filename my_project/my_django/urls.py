# Файл хранит URL пути которые будут использоваться только для текущего приложения my_django

# django
from django.urls import path, include

# my_project
from my_django.views import my_view2

urlpatterns = [
    # name позволяет обращаться к етому url-адресу в коде 
    path("my_view2/", my_view2, name="my_view2"),
]
