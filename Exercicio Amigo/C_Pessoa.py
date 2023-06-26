class Pessoa:
    def __init__(self, N, T):
        self.__Nome = N
        self.__Telef = T
    def LerNome(self):
        return self.__Nome
    def LerTelef(self):
        return self.__Telef
    def Impressao(self):
        return f"{self.LerNome()} -- {self.LerTelef()} --"