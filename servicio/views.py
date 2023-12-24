from django.shortcuts import render

from rest_framework import viewsets
from .serializer import ConvenioSerializer, EspecialistaSerializer, EspecialidadSerializer, ServicioSerializer, ConsultaSerializer, CategoriaConvenioSerializer,EspecialistaEspecialidadSerializer,EspecialidadServicioSerializer, EspecialistaConvenioSerializer
from .models import Convenio, Especialista, Especialidad, Servicio, Consulta, Categoria_convenio, Especialista_especialidad, Especialidad_servicio,Especialista_convenio  
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class ConvenioViewSet(viewsets.ModelViewSet):
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer

    def list(self, request):
        """
        List all convenios.
        """
        convenios = Convenio.objects.all()
        serializer = ConvenioSerializer(convenios, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new convenio.
        """
        serializer = ConvenioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a convenio.
        """
        convenio = Convenio.objects.get(pk=pk)
        serializer = ConvenioSerializer(convenio)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a convenio.
        """
        convenio = Convenio.objects.get(pk=pk)
        serializer = ConvenioSerializer(convenio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a convenio.
        """
        convenio = Convenio.objects.get(pk=pk)
        convenio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EspecialistaViewSet(viewsets.ModelViewSet):
    queryset = Especialista.objects.all()
    serializer_class = EspecialistaSerializer

    def list(self, request):
        """
        Listar todos los especialistas.
        """
        especialistas = Especialista.objects.all()
        serializer = EspecialistaSerializer(especialistas, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Crea un nuevo especialista.
        """
        serializer = EspecialistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Recuperar un especialista.
        """
        especialista = Especialista.objects.get(pk=pk)
        serializer = EspecialistaSerializer(especialista)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Actualizar un especialista.
        """
        especialista = Especialista.objects.get(pk=pk).prefetch_related('especialidades')
        serializer = EspecialistaSerializer(especialista, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Eliminar un especialista.
        """
        especialista = Especialista.objects.get(pk=pk)
        especialista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

    def list(self, request):
        """
        List all especialidades.
        """
        especialidades = Especialidad.objects.all()
        serializer = EspecialidadSerializer(especialidades, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new especialidad.
        """
        serializer = EspecialidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a especialidad.
        """
        especialidad = Especialidad.objects.get(pk=pk)
        serializer = EspecialidadSerializer(especialidad)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a especialidad.
        """
        especialidad = Especialidad.objects.get(pk=pk)
        serializer = EspecialidadSerializer(especialidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a especialidad.
        """
        especialidad = Especialidad.objects.get(pk=pk)
        especialidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ServicioViewSet(viewsets.ModelViewSet):

    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

    def list(self, request):
        """
        List all servicios.
        """
        servicios = Servicio.objects.all()
        serializer = ServicioSerializer(servicios, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new servicio.
        """
        serializer = ServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a servicio.
        """
        servicio = Servicio.objects.get(pk=pk)
        serializer = ServicioSerializer(servicio)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a servicio.
        """
        servicio = Servicio.objects.get(pk=pk)
        serializer = ServicioSerializer(servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a servicio.
        """
        servicio = Servicio.objects.get(pk=pk)
        servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def list(self, request) :
        """
        List all productos.
        """
        consultas = Consulta.objects.all()
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new producto.
        """
        serializer = ConsultaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a producto.
        """
        consulta = Consulta.objects.get(pk=pk)
        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a producto.
        """
        consulta = Consulta.objects.get(pk=pk)
        serializer = ConsultaSerializer(consulta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a producto.
        """
        consulta = Consulta.objects.get(pk=pk)
        consulta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriaConvenioViewSet(viewsets.ModelViewSet):
    queryset = Categoria_convenio.objects.all()
    serializer_class = CategoriaConvenioSerializer


    def list(self, request):
        """
        List all CategoriaConvenio.
        """
        categorias = Categoria_convenio.objects.all()
        serializer = CategoriaConvenioSerializer(categorias, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new CategoriaConvenio.
        """
        serializer = CategoriaConvenioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a producto.
        """
        categoria = Categoria_convenio.objects.get(pk=pk)
        serializer = CategoriaConvenioSerializer(categoria)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a producto.
        """
        categoria = Categoria_convenio.objects.get(pk=pk)
        serializer = CategoriaConvenioSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a producto.
        """
        categoria = Categoria_convenio.objects.get(pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class EspecialidadServicioViewSet(viewsets.ModelViewSet):
    queryset = Especialidad_servicio.objects.all()
    serializer_class = EspecialidadServicioSerializer

    
    def list(self, request):
        """
        List all EspecialidadServicio
        """
        categorias = Especialidad_servicio.objects.all()
        serializer = EspecialidadServicioSerializer(categorias, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new EspecialidadServicio
        """
        serializer = EspecialidadServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a EspecialidadServicio
        """
        categoria = Especialidad_servicio.objects.get(pk=pk)
        serializer = EspecialidadServicioSerializer(categoria)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a EspecialidadServicio
        """
        categoria = Especialidad_servicio.objects.get(pk=pk)
        serializer = EspecialidadServicioSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a EspecialidadServicio.
        """
        categoria = Especialidad_servicio.objects.get(pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EspecialistaConvenioViewSet(viewsets.ModelViewSet):
    queryset = Especialista_convenio.objects.all()
    serializer_class = EspecialistaConvenioSerializer

    
    def list(self, request):
        """
        List all EspecialistaConvenio.
        """
        categorias = Especialista_convenio.objects.all()
        serializer = EspecialistaConvenioSerializer(categorias, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new EspecialistaConvenio.
        """
        serializer = EspecialistaConvenioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a EspecialistaConvenio.
        """
        categoria = Especialista_convenio.objects.get(pk=pk)
        serializer = EspecialistaConvenioSerializer(categoria)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a EspecialistaConvenio.
        """
        categoria = Especialista_convenio.objects.get(pk=pk)
        serializer = EspecialistaConvenioSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a EspecialistaConvenio.
        """
        categoria = Especialista_convenio.objects.get(pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class EspecialistaEspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialista_especialidad.objects.all()
    serializer_class = EspecialistaEspecialidadSerializer

    def list(self, request):
        """
        List all especialistaEspecialidad.
        """
        categorias = Especialista_especialidad.objects.all()
        serializer = EspecialistaEspecialidadSerializer(categorias, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new especialistaEspecialidad.
        """
        serializer = EspecialistaEspecialidadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Retrieve a especialistaEspecialidad.
        """
        categoria = Especialista_especialidad.objects.get(pk=pk)
        serializer = EspecialistaEspecialidadSerializer(categoria)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Update a especialistaEspecialidad.
        """
        categoria = Especialista_especialidad.objects.get(pk=pk)
        serializer = EspecialistaEspecialidadSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """
        Delete a especialistaEspecialidad.
        """
        categoria = Especialista_especialidad.objects.get(pk=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
