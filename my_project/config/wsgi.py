# Файл хранит настройки чтоб веб-сервер смог запустить наш django-проект
# 
# WSGI - ето интерфес взаемодействия нашего django-проекта и веб-сервера(Nginx) на котором он будет работать
# 
# NGINX - ето сам веб-сервер на котором будет работать наш django-проект
# 
# WSGI взаемодействует с Apache, Nginx , Gunicorn


"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
