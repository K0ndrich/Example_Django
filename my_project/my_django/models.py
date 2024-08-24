# Файл хранит модели(таблици баз данных) нашего текущего приложения

# django
from django.db import models


# -----   МЕНЕДЖЕРЫ МОДЕЛЕЙ   ------------------------------------------------------------------------------------------------------------------------------------------------------


# создание возможности возвращать набор значений, создаем для нашего пользовательского менеджера запросов
class MyModel1QuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)

    def name(self):
        return self.filter(name="kondrich")


# создание своего менеджера моделей
class MyModel1Manager(models.Manager):

    # возвращает все ячейки модели
    def get_queryset(self):
        return MyModel1QuerySet(self.model)

    def published(self):  # -> MyModel1.
        # published взят из MyModel1QuerySet
        # return super().get_queryset().filter(is_published=True) можна также по такому
        return self.get_queryset().published()

    def name(self):
        # name взят из MyModel1QuerySet
        return self.get_queryset().name()


# -----   МОДЕЛИ   ------------------------------------------------------------------------------------------------------------------------------------------------------


# создаем свою модель
class MyModel1(models.Model):
    # создаем колонки для нашей модели
    my_number = models.IntegerField()
    # max_length=255 указывает макисмальну длину текста в 255 символов
    name = models.CharField(max_length=255)

    # 1) Отношение --- Один к Одному ---
    # В первой таблице значение НЕ может повторяться, а во второй тоже НЕ может
    # my_column3 = models.OneToOneField(MyModel2, on_delete=models.PROTECT, null=True)
    #
    #
    # 2) Отношение --- Один ко Многим ---
    # В первой таблице значение НЕ может повторяться, а во второй Может
    # null=True разрешает помещать в ячейку значение NULL
    is_published = models.ForeignKey("MyModel2", on_delete=models.PROTECT, null=True)

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

    # указываме свой новый менеджер, можно использовать два менеджера одновременно
    objects = models.Manager  # по умолчанию
    my_manager = MyModel1Manager()

    # теперь можно + обращаться так
    # -> MyModel1.my_manager().published()
    # -> MyModel1.my_manager().name()
    # -> MyModel1.my_manager().published().name()


# на ету модель ссылкаеться MyModel1
class MyModel2(models.Model):

    is_published = models.BooleanField(null=True, blank=True)
