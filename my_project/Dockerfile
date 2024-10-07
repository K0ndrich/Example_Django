# Docker
# Файл хранит настройки для одного текущего docker-контейнера

# FROM берем образ на котором будет работать текущий один docker-контейнер
FROM python:3.11-slim

# создаем папку и указываем что ето рабочая директория
# ето папка также хранит путь папки хоста текузего контейнера,
# куда будут передаваться даныне через docker volumes, если не добавить другой веб-сервер(например nginx)
WORKDIR /app

# копируем все файлы из нашего локального проекта внутрь контейнера
# локальные файлы проекта  -  внутри нашего контейнера
COPY . /app/

# RUN выполняет команды во время создания docker-образа из которого будет запущен наш контейнер
# обновление пакетов debian 
# RUN apt-get update && apt-get install -y curl && apt-get clean

# обновление для python пакетого менеджера pip
RUN pip install --upgrade pip

# установка зависимостей к проекту
RUN pip install -r req.txt

# CMD выполняет команды уже внутри запущеного текущего docker-контейнера
# && python manage.py shell -c создание суперпользователя, если его нету login->root   password->1234
# && python manage.py initialize_db создание базы данных для проекта внутри контейнера
# && python manage.py collectstatic берет все сатические файлы и переносит внутрь STATIC_ROOT , чтоб NGINX мог с ними работать и отдавть клиенту на сайт
CMD python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='kondrich').exists() or User.objects.create_superuser('kondrich', '123kondrich@gmail.com', '1234')" \
    && python manage.py collectstatic
    && python manage.py runserver 0.0.0.0:8000
    # && python manage.py initialize_db \  (НЕ РАБОТАТЕ - ВЫДАЕТ ОШИБКУ)
    # && python manage.py collectstatic --no-input \
    # && gunicorn prediction.wsgi:application --bind 0.0.0.0:8000 --log-level info







# -----   ПРОСТО ПОДСКАЗКИ ДЛЯ DOCKER (НЕ ИСПОЛЬЗУЕМ)   ------------------------------------------------------------------------------------------------------------------------------------------------

# FROM берем образ на котором будет работать текущий один docker-контейнер
# FROM python:3.11-slim

# # RUN выполняет команды во время создания docker-образа
# # создаем папку, где будем хранить наш проект 
# RUN mkdir my_project

# # указываем что наша новосозданая папка будет рабочей директорией нашего docker-образа
# WORKDIR my_project

# # берем все файлы из нашего проекта и помещаем в docker-контейнера
# # ADD откуда - куда
# ADD . /my_project/

# # перемещаем наш файл с пременными окружения локальными в файл с переменными окружения для docker-контейнера 
# ADD .env.docker /my_project/.env

# # ENV создает новые переменные оружения внутри .env.docker файла
# ENV APP_NAME = MY_PROJECT

# # скачиваем наши зависимости для нашего docker-образа
# RUN pip install -r req.txt

# # запуск проекта на веб-сервере
# # CMD gunicorn config.wsgi:application -b 0.0.0.0:8000
# CMD python manage.py runserver

# # CMD указывает действия которые будут выполняться при запуске текущего docker-контейнера
# # CMD python test.py 



