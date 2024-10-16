# Файл хранит преставления страниц и/или нашего API


# django
from django.shortcuts import render
from django.views.generic.list import ListView

from rest_framework.viewsets import ModelViewSet

# my_project
from my_django.models import MyModel1


# представление основаное на функции
def my_view(request):
    # request - наш запрос (просто вписываеться)
    # template_name - название шаблона, которые будем использовать в текущем представлении
    # context = my_data - по етому слову будем использовать данные из таблици MyModel1 в index.html
    return render(
        request=request,
        template_name="index.html",
        context={"my_data": MyModel1.objects.all()},
    )


def my_expression(request):
    return render(request, template_name="my_django/my_expression.html")


# представление основаное на классе
# ListView предназначен для вывода списка обьктов модели
class MyView(ListView):
    pass
