#Classe que representa a entidade clienteFisico

from Cliente import Cliente


class ClienteFisico(Cliente):
    cpf = ''

    def __init__(self, nome, endereco, telefone, cpf):
        super.__init__(nome, endereco, telefone)

        self.cpf = cpf



    def getCpf(self):
        return self.cpf

    def setCpf(self,cpf):
        self.cpf = cpf
        


