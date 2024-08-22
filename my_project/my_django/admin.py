# Файл для управления панелью адиминастратора и регистрации моделей в етой админ-панели

# django
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# my_project
from my_django.models import MyModel1, MyModel2


# регистрация нашей модели в админ-панели через функцию
admin.site.register(MyModel1)


# регистрация модели в админ-панели через декоратор
@admin.register(MyModel2)
class BookAdmin(admin.ModelAdmin):
    pass


