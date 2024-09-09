# Файл хранит Переменные-Настройки для нашего django проекта


"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

# os подключаем для того чтоб задавать пути для файлов в нашем проекте через os.path.join()
import os

from pathlib import Path

# для работы с перемеными окружения
import environ


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()
# прописываем путь до нашого файла .env , который хранит переменные среды
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# берем значенние переменной среды из .env файла
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True режим дебага включен, нужно выключать при деплое
DEBUG = env("DEBUG")

# '*' означает запуск на любих ip-адресах
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # django.contrib.admin нужен для управления админ-панелью
    "django.contrib.admin",
    # django.contrib.auth нужен для управления таблици, которая хранит пользователей
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # подключаем наши приложения к проекту
    "my_django",
    "my_django_rest",
    # rest_framework подключаем django_rest к проекту
    "rest_framework",
    # дополнительный функционал для нашего django
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# указываем где храниться основной файл с главные(начальными) URL путями для всего проекта
ROOT_URLCONF = "config.urls"

# TEMPLATES хранит пути местоположения шаблонов, которые будут импользоваться в представлениях views.py
TEMPLATES = [
    {
        # # указываем имя для шаблонизатора
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # указываем путь к папке с шаблонами или просто название папки
        "DIRS": ["templates"],
        # "APP_DIRS": True  ищет по умолчанию шаблоны в my_project/templates/index.html
        "APP_DIRS": True,
        "OPTIONS": {
            # контекстные процессоры
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES подключение баз данных к нашему проекту
DATABASES = {
    #
    #
    # Покдлючение к базе PostgreSQL, которая лежит внутри контейнера (docker-compose.yml)
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": os.environ.get("DB_NAME"),
    #     "USER": os.environ.get("DB_USER"),
    #     "PASSWORD": os.environ.get("DB_PASSWORD"),
    #     "HOST": os.environ.get("DB_HOST"),
    #     "PORT": os.environ.get("DB_PORT"),
    # }
    #
    # Подключение к базе SQLite
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    
    
}




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# указывает язык для нашего проекта
LANGUAGE_CODE = "en-us"

# указывает часовой пояс для нашего проекта
TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


# STATIC_URL хранить путь URL по которому в браузере можно будует отобразить наши static(статические) файлы
STATIC_URL = "static/"

# STATICFILES_DIRS хранит путь, где в нашем проекте лежит папка static c статическими файлами (css , js)
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# удаляет возможность пользователям искать информацию django rest вводя команды в url-адрессе сайта
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        # "rest_framework.renderers.BrowsableAPIRenderer", ->  если строка закоментирована, тогда вписывать в url-адресс ничего нельзя
        "rest_framework.renderers.BrowsableAPIRenderer",
    ]
}
