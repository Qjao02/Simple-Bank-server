from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework import  serializers

from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Cliente
        depth = 1  
        fields = ['id','nome','endereco','cadastroDatetime','origem_funcionario_id']
        

    