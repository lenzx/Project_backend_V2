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
    especialista_convenio = EspecialistaSerializer(read_only = True, many=True)
    class Meta:
        model = Convenio
        fields = '__all__'
    
    # def update(self, instance, validated_data):
    #     especialistas_data = validated_data.pop('especialista_convenio', [])
    #     instance.nombre = validated_data.get('nombre', instance.nombre)
    #     instance.save()

    #     for especialista_data in especialistas_data:
    #         especialista_id = especialista_data.get('id')
    #         if especialista_id:
    #             Especialista.objects.filter(id=especialista_id).update(**especialista_data)
    #         else:
    #             Especialista.objects.create(convenio=instance, **especialista_data)

    #     return instance

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
