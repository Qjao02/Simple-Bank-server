from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework import  serializers

from .models import Cliente, Funcionario, Administrador

class ClienteSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Cliente
        depth = 1  
        fields = ['id','nome','data_cadastro','rua_mora','cidade_mora','estado_mora','funcionario_cadastrou']

        

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        #Profundidade
        depth = 1
        fields = [ 'id','login','senha','data_cadastro','adm_cadastrou']




class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        depth = 1
        fields = ['id','login','senha','agencia']

