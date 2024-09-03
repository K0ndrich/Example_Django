# Свое Пользователськое API-Представление

# my_project
from rest_framework.views import APIView


# APIView унаследуемся от базового класса, стоит во главе иерархии
class WomenAPIView(APIView):

    # метод обрабатыает get-запросы от пользователя к сайту
    def get(self, request):

        my_objects = Women.objects.all()

        # 1) ВАРИАНТ
        # many=True указываем что сериализатору нужно оборабатывать не одну запись, а набор записей
        return Response(
            {"posts": WomenSerializer(my_objects, many=True).data}
        )  # -> {"posts":[{"title":"Women_1","cat_id":1},{"title":"Women_2","cat_id":2},{"title":"Women_3","cat_id":1},{"title":"Women_4","cat_id":1},{"title":"Oleksey","cat_id":2},{"title":"my_name","cat_id":2}]}

        # 2) ВАРИАНТ
        # возвращает ответ в типе django_rest
        # return Response({"my_get_request": "Kondrich"})

    # метод обрабатывает post-запросы от пользователя к сайту, добавление новой ячейки в базу
    def post(self, request):

        # розпоковываем json строку полученую из url-адресса в список словарей
        serializer = WomenSerializer(data=request.data)
        # проверка на уровне сериализатора правильно ли указаны все параметры в url-адресе
        # ловим ошибку, которая вылетит
        serializer.is_valid(
            raise_exception=True
        )  # -> "title": ["Ето поле обязательное"]

        # 1) ВАРИАНТ С МЕТОДОМ -CREATE- СЕРИАЛИЗАТОРА
        # добавление текущей новой ячейки в базу данных
        # сохранение ячейки в базе
        serializer.save()

        # 2) ВАРИАНТ БЕЗ МЕТОДА СЕРИАЛИЗАТОРА
        # post_new = Women.objects.create(
        #     # request.data["title"] ето значения которие мы прописываев в url-адресе при post-запросе
        #     title=request.data["title"],
        #     content=request.data["content"],
        #     cat_id=request.data["cat_id"],
        # )

        return Response(
            {"posts": serializer.data}
        )  # -> {"posts":{"title":"my_name","cat_id":2}}

    # перезаписывает запись в базе данных
    # вызывает метод update из нашего сериализатора
    def put(self, request, *args, **kwargs):

        pk = kwargs.get("pk", None)

        # если нету id-ключа pk возвращаем ошибку
        if not pk:
            return Response({"ERROR": "Method PUT not allowed"})

        try:

            # берем запись из базы по id-ключу pk
            instance = Women.objects.get(pk=pk)

        except:

            return Response({"ERROR": "This PK object is not allowed"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    # удаление существующей ячейки в базе данных (удаляет ее из базы)
    def delete(self, request, *args, **kwargs):

        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"ERROR": "Method DELETE not allowed"})

        try:
            instance = Women.objects.get(pk=pk)

        except:
            return Response({"ERROR": "This PK object is not allowed"})

        # само удаление ячейки из базы
        instance.delete()

        return Response({"post": "Delete post -> " + str(pk)})
