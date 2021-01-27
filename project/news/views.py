from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from .models import News
from .serializers import NewsListSerializer


class NewsListView(ListAPIView):
    """
    Вывод списка новостей
    """
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    filter_backends = (OrderingFilter, )
    ordering_fields = '__all__'
