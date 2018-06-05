from rest_framework import  serializers
import sys
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        depth = 1   
        fields = ['id','nome','endereco','telefone','conta']