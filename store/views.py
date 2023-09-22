from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


@api_view(['GET'])
def category_list(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer.CateogrySerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)