from rest_framework import viewsets
from .serializer import SeccionSerializer, MarkaySerializer, Red_socialSerializer
from .models import Seccion, Markay, Red_social
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class MarkayViewSet(viewsets.ModelViewSet) :
    queryset = Markay.objects.all()
    serializer_class = MarkaySerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request) :
        """
        List all productos.
        """
        markays = Markay.objects.all() 
        serializer = MarkaySerializer(markays, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new producto.
        """
        serializer = MarkaySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a producto.
        """
        markay = Markay.objects.get(pk=pk) 
        serializer = MarkaySerializer(markay)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a producto.
        """
        markay = Markay.objects.get(pk=pk) 
        serializer = MarkaySerializer(markay, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a producto.
        """
        markay = Markay.objects.get(pk=pk) 
        markay.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SeccionViewSet(viewsets.ModelViewSet) :
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        """
        List all productos.
        """
        secciones = Seccion.objects.all() 
        serializer = SeccionSerializer(secciones, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new producto.
        """
        serializer = SeccionSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a producto.
        """
        seccion = Seccion.objects.get(pk=pk) 
        serializer = SeccionSerializer(seccion)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a producto.
        """
        seccion = Seccion.objects.get(pk=pk) 
        serializer = SeccionSerializer(seccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a producto.
        """
        seccion = Seccion.objects.get(pk=pk) 
        seccion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class RedSocialViewSet(viewsets.ModelViewSet):
    queryset = Red_social.objects.all()
    serializer_class = Red_socialSerializer
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        """
        List all productos.
        """
        redsociales = Red_social.objects.all()
        serializer = Red_socialSerializer(redsociales, many=True)
        return Response(serializer.data)

    def create(self, request) :
        """
        Create a new producto.
        """
        serializer = Red_socialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """
        Retrieve a producto.
        """
        redsocial = Red_social.objects.get(pk=pk)
        serializer = Red_socialSerializer(redsocial)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a producto.
        """
        redsocial = Red_social.objects.get(pk=pk)
        serializer = Red_socialSerializer(redsocial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk=None) :
        """
        Delete a producto.
        """
        redsocial = Red_social.objects.get(pk=pk)
        redsocial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
