
from rest_framework import serializers

from .models import (
    Red_social, Markay, Seccion, 
)

class MarkaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Markay
        fields = '__all__'

class SeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seccion
        fields = '__all__'

class Red_socialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Red_social
        fields = '__all__'
