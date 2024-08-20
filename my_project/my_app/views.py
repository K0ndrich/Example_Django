# Файл хранит преставления страниц и/или нашего API


# django
from django.shortcuts import render

# my_project
from my_app.models import MyModel1


# представление основаное на функции
def my_view(request):
    # request - наш запрос (просто вписываеться)
    # template_name - название шаблона, которые будем использовать в текущем представлении
    # context = my_data - по етому слову будем использовать данные из таблици MyModel1 в index.html
    return render(
        request=request,
        template_name="index.html",
        context={"my_data": MyModel1.objects.all()},
    )


# представление основаное на функции
def my_view2(request):
    return render(request=request, template_name="index2.html")


# создание API через наш django_rest
class OrderView(ModelViewSet):
    # queryset хранит значения елементов которые мы будем выводить в api
    queryset = SalesOrder.objects.all()
    # serializer_class указывает каким сериализатором будем обрабатывать значения и выводить их
    serializer_class = OrderSerializer
