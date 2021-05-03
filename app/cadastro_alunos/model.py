class Pessoas: 
    def __init__(self, nome, email, cpf, senha):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf
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

    def getsenha(self):
        return self.__senha

class Alunos(Pessoas):
    def __init__(self, nome, email, cpf, senha, dre, curso):
        super().__init__(nome,email,cpf,senha)
        self.__dre = dre
        self.__curso = curso
  
    def getdre(self):
        return self.__dre
  
    def setdre(self,dre):
        self.__dre = dre
  
    def getcurso(self):
        return self.__curso
  
    def setcurso(self,curso):
        self.__curso = curso