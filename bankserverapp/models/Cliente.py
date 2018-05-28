#Cliente modelo, define a estrutura da entidade cliente

from Telefone import Telefone

class Cliente:

    nome = ''
    endereco = ''
    telefone = ''


    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = Telefone(telefone.tel1, telefone.tel2)

    

    
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