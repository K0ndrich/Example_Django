# Файл хранит преставления страниц и/или нашего API


# django
from django.http import HttpRequest, HttpResponse
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


# представление основаное на функции по-другому
def my_view2(request):
    return render(request, template_name="index2.html")


# представление основаное на классе
# ListView предназначен для вывода списка обьктов модели
class MyView(ListView):
    pass


# REQUEST хранит запрос к сайту от пользователя
# Сайт -> https://docs.djangoproject.com/en/5.1/ref/request-response/
def my_request_data(request):

    # содержит путь к нашему представлению
    path = request.path  # -> /my_request_data/
    # содержит мето обращения к серверу
    method = request.method  # -> GET / POST
    # хранит словарь, который содержит все парамаетры нашего get-запрсоа
    get = request.GET  
    # хранит словарь, который содержит все парамаетры нашего post-запрсоа
    post = request.POST
    # хранит значение пользоваетльского агента
    user_agent = request.META["HTTP_USER_AGENT"]  # -> Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
    return HttpResponse(user_agent)
