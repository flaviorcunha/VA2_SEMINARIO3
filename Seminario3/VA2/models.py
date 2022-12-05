from django.db import models

from django.db import models

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    CPF = models.CharField(max_length=11)

def __str__(self):
    return self.nome_cliente
