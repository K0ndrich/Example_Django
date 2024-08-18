# Файл хранит преставления страниц и/или нашего API
from django.shortcuts import render


# представление основаное на функции
def my_view(request):
    return render(request=request, template_name="index.html")


# представление основаное на функции
def my_view2(request):
    return render(request=request, template_name="index2.html")