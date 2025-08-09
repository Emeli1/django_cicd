from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    orderind_fields = ['id']
    pagination_class = LimitOffsetPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['id']
    orderind_fields = ['id']
    pagination_class = LimitOffsetPagination


@api_view(['GET'])
def sample_view(request):
    return Response({'message': 'Это новая версия!!!'})