class Pessoas: 
    def __init__(self, nome, cpf, email, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__senha = senha

    def salva(self  ):
        registro = self.__user + " - " +self.__senha  + " \n"
        arquivo = open("registro_aluno.txt","a")
        arquivo.writelines(registro)

    def setcpf(self,email):
        self.__email = email
    
    def getcpf(self):
        return self.__email 
    
    def setcpf(self,cpf):
        self.__cpf = cpf
    
    def getcpf(self):
        return self.__cpf

class Professores(Pessoas):
    def __init__(self, nome, cpf, email, senha, siape):
        super().__init__(nome,cpf,email,senha)
        self.__siape = siape
  
    def getsiape(self):
        return self.__siape
  
    def setsiape(self,siape):
        self.__siape = siape
