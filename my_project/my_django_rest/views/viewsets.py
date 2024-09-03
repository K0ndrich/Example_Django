# Viewsets ето наборы API-Предствалений
# Viewsets дают возможность пользователю взаемодействовать не с типами запросом, а с целыми методами действий с базой данных
# Viewsets обединяет все типы запросов внутри себя и дает методы(действия) над етими запросами

# django_rest
from rest_framework.viewsets import ModelViewSet

# my_project
from my_django_rest.models import Women
from my_django_rest.serializers.main_serializers import WomenSerializer


# ModelViewSet набор представлений для работы с моделью
class WomenViewSet(ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

  