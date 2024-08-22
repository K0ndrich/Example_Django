from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    # blank указывает можно ли заполнять пустым значением
    content = models.TextField(blank=True)
    # auto_now_add харнит время создания значения ячейки
    time_create = models.DateTimeField(auto_now_add=True)
    # auto_now хранит время изменения значения ячейки
    time_update = models.DateTimeField(auto_now=True)
    # default указывает значение по умолчанию
    is_published = models.BooleanField(default=True)
    # отношение одик ко многим
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    # db_index cсоздает индекс для поля, берет значения из ячеек быстрее
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
