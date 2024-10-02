# REQUEST хранит запрос к сайту от пользователя

# Сайт -> https://docs.djangoproject.com/en/5.1/ref/request-response/

from django.http import HttpRequest, HttpResponse


def my_request_data(request):

    # содержит путь к нашему представлению
    path = request.path  # -> /my_request_data/
    # содержит метод обращения к серверу
    method = request.method  # -> GET / POST
    # хранит словарь, который содержит все парамаетры нашего get-запрсоа
    get = request.GET
    # хранит словарь, который содержит все парамаетры нашего post-запрсоа
    post = request.POST
    # хранит значение пользовательского агента
    user_agent = request.META[
        "HTTP_USER_AGENT"
    ]  # -> Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36
    return HttpResponse(user_agent)
