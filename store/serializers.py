from rest_framework import serializers
from.import models
class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    class Meta:
        model= models.Product