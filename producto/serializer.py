from rest_framework import serializers
from .models import (
    Categoria, Producto_categoria, Producto
)
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto_categoria
        fields = '__all__'
