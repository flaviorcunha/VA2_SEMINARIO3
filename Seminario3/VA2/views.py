from rest_framework import viewsets
from VA2.models import Cliente
from VA2.serializer import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


