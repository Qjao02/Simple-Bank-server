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
    
