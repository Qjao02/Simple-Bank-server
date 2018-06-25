from django.db import models

# Create your models here.

class Agencia(models.Model):
    nome = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 200)
    banco_id = models.IntegerField()


class Administrador(models.Model):
    
    login = models.CharField(max_length = 45)
    senha = models.CharField(max_length = 45)
    agencia = models.CharField(max_length = 45)

class Funcionario(models.Model):
        #login,senha,data_cadastro,adm_cadastrou

    login = models.CharField(max_length = 15)
    senha = models.CharField(max_length = 15)
    data_cadastro = models.DateField()
    adm_cadastrou = models.CharField(max_length = 50)



class Cliente(models.Model):
    
        #data_cadastro,nome,rua_mora,cidade_mora,estado_mora,funcionario_cadastrou

    nome = models.CharField(max_length = 50)
    rua_mora = models.CharField(max_length = 45)
    cidade_mora = models.CharField(max_length = 45)
    estado_mora = models.CharField(max_length = 45)     
    funcionario_cadastrou = models.CharField(max_length = 45)  
    data_cadastro = models.DateField()    
        




