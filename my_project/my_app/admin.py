# Файл для управления панелью адиминастратора и регистрации моделей в етой панели


from django.contrib import admin
from my_app.models import MyModel1, MyModel2

# регистрация нашей модели в админ-панели
admin.site.register(MyModel1)
admin.site.register(MyModel2)
