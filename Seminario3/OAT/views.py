from rest_framework import viewsets
from OAT.models import Professor
from OAT.serializer import ProfessorSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

