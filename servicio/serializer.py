from rest_framework import serializers
from .models import (
    Convenio, Especialidad, Especialista, Servicio,
    Categoria_convenio, Consulta, Especialista_convenio, Especialista_especialidad,
    Especialidad_servicio
)

class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = '__all__'

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class EspecialistaSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer(read_only= True, many=True)

    class Meta:
        model = Especialista
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class EspecialidadServicioSerializer(serializers.ModelSerializer):
    especialista = EspecialistaSerializer(read_only= True, many=True)
    servicio = ServicioSerializer(read_only= True, many=True)

    class Meta:
        model = Especialidad_servicio
        fields = '__all__'

class CategoriaConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_convenio
        fields = '__all__'
    

class EspecialistaConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialista_convenio
        fields = '__all__'

class EspecialistaEspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialista_especialidad
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'