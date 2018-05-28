#Classe que representa a entidade Cliente Juridicoo

from Cliente  import Cliente

class ClienteJuridico(Cliente):
    cnpj = ''

    def __init__(self, nome, endereco, telefone, cnpj):
        super.__init__(nome, endereco, telefone)

        self.cnpj = cnpj


