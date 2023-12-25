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
    especialista_convenio = EspecialistaSerializer(read_only=True, many=True)
    class Meta:
        model = Convenio
        fields = '__all__'
    
    def create(self, validated_data):
        especialistas_data = validated_data.pop('especialista_convenio')
        convenio = Convenio.objects.create(**validated_data)
        for especialista_data in especialistas_data:
            Especialista.objects.create(convenio=convenio, **especialista_data)
        return convenio

    def update(self, instance, validated_data):
        especialistas_data = validated_data.pop('especialista_convenio')
        especialistas = (instance.especialista_convenio).all()
        especialistas = list(especialistas)

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.save()

        for especialista_data in especialistas_data:
            especialista = especialistas.pop(0)
            especialista.nombre = especialista_data.get('nombre', especialista.nombre)
            especialista.save()

        return instance


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'

class CategoriaConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_convenio
        fields = '__all__'
    

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'