from rest_framework import serializers
from VA2.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:

        model = Cliente
        fields = '__all__'