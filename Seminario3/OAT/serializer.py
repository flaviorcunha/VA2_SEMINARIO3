from rest_framework import serializers
from OAT.models import Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:

        model = Professor
        fields = '__all__'