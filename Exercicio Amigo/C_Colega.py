from C_Pessoa import *
class Colega(Pessoa):
    def __init__(self, N, T, P, LT):
        super().__init__(N, T)
        self.__Profissao=P
        self.__LocalTab=LT
    def LerProf(self):
        return self.__Profissao
    def LerLTrab(self):
         return self.__LocalTab