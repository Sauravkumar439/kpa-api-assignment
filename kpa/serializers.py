from rest_framework import serializers
from .models import KPAFormData, User

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

class KPAFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = KPAFormData
        fields = '__all__'
