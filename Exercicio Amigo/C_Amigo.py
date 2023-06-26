from C_Pessoa import *
class Amigo(Pessoa):
    def __init__(self, N, T, L, A):
        super().__init__(N, T)
        self.__Local=L
        self.__Ano=A
    def LerLocal(self):
        return self.__Local
    def LerAno(self):
        return self.__Ano
    def ImpressaoA(self):
        print(super().Impressao(),self.LerLocal(),"--", self.LerAno())
        return