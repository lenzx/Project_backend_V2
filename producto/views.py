from django.shortcuts import render

from rest_framework import viewsets
from .serializer import ProductoSerializer, CategoriaSerializer, ProductoCategoriaSerializer
from .models import Producto, Categoria, Producto_categoria  
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request):
        """
        List all productos.
        """
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new producto.
        """
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a producto.
        """
        producto = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a producto.
        """
        producto = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a producto.
        """
        producto = Producto.objects.get(pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def list(self, request):
        """
        List all categorias.
        """
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new categoria.
        """
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a categoria.
        """
        categoria = Categoria.objects.get(pk=pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a categoria.
        """
        categoria = Categoria.objects.get(pk=pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a categoria.
        """
        categoria = Categoria.objects.get(pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductoCategoriaViewSet(viewsets.ModelViewSet):
    queryset = Producto_categoria.objects.all()
    serializer_class =  ProductoCategoriaSerializer

    def list(self, request):
        """
        List all ProductoCategoria
        """
        categorias = Producto_categoria.objects.all()
        serializer =  ProductoCategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a ProductoCategoria
        """
        serializer =  ProductoCategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a ProductoCategoria
        """
        categoria = Producto_categoria.objects.get(pk=pk)
        serializer =  ProductoCategoriaSerializer(categoria)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a ProductoCategoria
        """
        categoria = Producto_categoria.objects.get(pk=pk)
        serializer = ProductoCategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a categoria.
        """
        categoria = Producto_categoria.objects.get(pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

