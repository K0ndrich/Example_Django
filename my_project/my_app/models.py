# Файл хранит модели(таблици баз данных) нашего текущего приложения


from django.db import models

# создаем свою модель
class MyModel1(models.Model):
    # создаем колонки для нашей модели
    my_column1 = models.IntegerField()
    # max_length=255 указывает макисмальну длину текста в 255 символов
    my_column2 = models.CharField(max_length=255)


# 1) Отношение --- Один к Одному ---
# В первой таблице значение НЕ может повторяться, а во второй тоже НЕ может

# 2) Отношение --- Один ко Многим ---
# В первой таблице значение НЕ может повторяться, а во второй Может

# 3) Отношение --- Многие ко Многим ---
# В первой таблице значение Может повторяться, а во второй тоже Может


# Один ко Многим
my_column3 = models.ForeignKey(MyModel2, on_delete=models.SET_NULL, null=True)


class MyModel2(models.Model):
    my_column1 = models.IntegerField()
    my_column2 = models.CharField(max_length=255)
