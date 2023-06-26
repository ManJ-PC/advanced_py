

class Pessoa():
    def __init__(self,Nome,Telm):
        self.Nome=Nome
        self.Telm=Telm
    def LerNome(self):
        return self.Nome
    def LerTelm(self):
        return self.Telm

class Amigo(Pessoa):
    def __init__(self,Nome,Telm,Local,Ano):
        super().__init__(Nome,Telm)
        self.Local=Local
        self.Ano=Ano
    def LerLocal(self):
        return self.Local
    def LerAno(self):
        return self.Ano
    
class Colega(Pessoa):
    def __init__(self,Nome,Telm,Local_T,Prof):
        super().__init__(Nome,Telm)
        self.Local_T=Local_T
        self.Prof=Prof
    def LerLocal_T(self):
        return self.Local_T
    def LerProf(self):
        return self.Prof