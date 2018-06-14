from django.db import models

# Create your models here.

class Telefone(models.Model) :
    telefone1 = models.CharField(max_length = 13)
    telefone2 = models.CharField(max_length = 13)

class Cliente(models.Model):
    
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length = 50)
    endereco = models.CharField(max_length = 100)
    cadastroDatetime = models.DateField()     
    origem_funcionario_id = models.IntegerField()

class Administrador(models.Model):
    login = models.CharField(max_length = 15)
    pwd = models.CharField(max_length = 15)


class ClienteFisico(Cliente):
    cpf = models.CharField(max_length = 11)

class ClienteJuridico(Cliente):
    cnpj = models.CharField(max_length = 11)

class Conta(models.Model):
    saldo = models.CharField(max_length = 50)
    senha = models.CharField(max_length = 50)

class Agencia(models.Model):
    endereco = models.CharField(max_length = 50)
    nome = models.CharField(max_length = 20)
'''




class Administrador:
    login = ''
    senha = ''

    def __init__(self, login,senha):
        self.login = login
        self.senha = senha


    def  getLogin(self):
        return self.login
    
    def setLogin(self, login):
        self.login = login


        #Classe que representa a entidade Agencia
class Agencia:
    endereco = ''
    nome = ''
    
    def __init__(self, endereco, nome):
        self.endereco = endereco
        self.nome = nome

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

        #Classe que representa o atributo multivalorado da classe cliente

class Telefone :
    tel1 = ''
    tel2 = ''

    def __init__(self, telefone1, telefone2):
        self.tel1 = telefone1
        self.tel2 = telefone2

    
    def getTel1(self):
        return self.tel1

    def setTel1(self, telefone1):
        self.tel1 = telefone1
    
    def getTel2(self):
        return self.tel2
    
    def setTel2(self, telefone2):
        self.tel2 = telefone2
    




        #Cliente modelo, define a estrutura da entidade cliente


class Cliente:

    nome = ''
    endereco = ''
    telefone = ''
    conta = ''


    def __init__(self, nome, endereco, telefone, conta):
        self.nome = nome
        self.endereco = endereco
        self.telefone = Telefone(telefone.tel1, telefone.tel2)
        self.conta = conta
    

    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome

    def getEndereco(self):
        return self.endereco

    def setEndereco(self,endereco):
        self.endereco = endereco

    def getTelefone(self, telefone):
        return self.telefone

    def setTelefone(self, telefone):
        self.telefone =telefone


        #Classe que representa a entidade clienteFisico



class ClienteFisico(Cliente):
    cpf = ''

    def __init__(self, nome, endereco, telefone, conta, cpf):
        super.__init__(nome, endereco, telefone,conta)

        self.cpf = cpf



    def getCpf(self):
        return self.cpf

    def setCpf(self,cpf):
        self.cpf = cpf




#Classe que representa a entidade Cliente Juridicoo

class ClienteJuridico(Cliente):
    cnpj = ''

    def __init__(self, nome, endereco, telefone, conta,  cnpj):
        super.__init__(nome, endereco, telefone, conta)

        self.cnpj = cnpj


        # Classe que representa a entidade conta

class Conta:
    saldo = ''
    senha = ''

    def __init__(self, senha):
        
        self.senha = senha
        self.saldo = 0

    

    def getSaldo(self):
        return self.saldo
    
        



  '''      





