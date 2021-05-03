class Pessoas: 
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    def setcpf(self,cpf):
        self.__cpf = cpf
    
    def getcpf(self):
        return self.__cpf

class professor(Pessoas):
    def __init__(self, nome, cpf, siape):
        super().__init__(nome,cpf)
        self.__siape = siape
  
    def getsiape(self):
        return self.__siape
  
    def setsiape(self,siape):
        self.__siape = siape
