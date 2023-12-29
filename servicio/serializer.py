from rest_framework import serializers
from .models import (
    Convenio, Especialidad, Especialista, Servicio,
    Categoria_convenio, Consulta
    
)
class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'


class EspecialistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialista
        fields = '__all__'

class ConvenioSerializer(serializers.ModelSerializer):
    especialista_convenio = EspecialidadSerializer(read_only = True, many=True)
    class Meta:
        model = Convenio
        fields = '__all__'
    

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class CategoriaConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_convenio
        fields = '__all__'
    

class ConsultaSerializer(serializers.ModelSerializer):
    especialista_id = serializers.PrimaryKeyRelatedField(queryset=Especialista.objects.all())
    class Meta:
        model = Consulta
        fields = '__all__'
    
class CustomConsultaSerializer(serializers.ModelSerializer):
    especialista_id = EspecialistaSerializer(read_only = True)
    class Meta:
        model = Consulta
        fields = '__all__'
