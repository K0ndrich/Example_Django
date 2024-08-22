# Файл хранит модели(таблици баз данных) нашего текущего приложения


from django.db import models


class MyModel2(models.Model):
    my_column1 = models.IntegerField()
    my_column2 = models.CharField(max_length=255)


# создаем свою модель
class MyModel1(models.Model):
    # создаем колонки для нашей модели
    my_column1 = models.IntegerField()
    # max_length=255 указывает макисмальну длину текста в 255 символов
    my_column2 = models.CharField(max_length=255)

    # 1) Отношение --- Один к Одному ---
    # В первой таблице значение НЕ может повторяться, а во второй тоже НЕ может
    # my_column3 = models.OneToOneField(MyModel2, on_delete=models.PROTECT, null=True)
    #
    #
    # 2) Отношение --- Один ко Многим ---
    # В первой таблице значение НЕ может повторяться, а во второй Может
    # null=True разрешает помещать в ячейку значение NULL
    my_column4 = models.ForeignKey(MyModel2, on_delete=models.PROTECT, null=True)

    # on_delete=models.SET_NULL -> когда удаляеться ячейка с первой текущей таблици MyModel1, тогда во второй таблице MyModel2 становить NULL
    # on_delete=models.CASCADE  -> когда удаляеться ячейка с первой текущей таблици MyModel1, тогда во второй таблице MyModel2 удяються все ячейки связанные с первой
    # on_delete=models.PROTECT  -> нельзя удалить ячейку из первой текущей таблици MyModel1, когда есть связаные с ней ячейки во второй таблице MyModel2
    #
    #
    # 3) Отношение --- Многие ко Многим ---
    # В первой таблице значение Может повторяться, а во второй тоже Может
    # my_column4 = models.ManyToManyField(MyModel2)

    # будет возвращать не object_1 , а значение нашей указаной колонки текущей ячейки
    def __str__(self):
        return f"velue -> {self.my_column1}"
