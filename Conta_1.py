

"""Depositos, levantamentos, consultas"""
class conta:
    def __init__(self,quantia):
        self.saldo=quantia
    
    def deposito(self,quantia):
        self.saldo=self.saldo+quantia
        return  self.saldo
    
    def consulta(self):
        return self.saldo
    
    def levantamento(self,quantia):
        if self.saldo-quantia >=0:
            self.saldo=self.saldo-quantia
            return self.saldo
        else:
            print('Saldo Insuficiente')
    

def cria_conta(saldo):
    return conta(saldo)
    
def consulta(c):
    return c.consulta()
    
def deposito(c,q):
        return c.deposito(q)
    
def levantamento(c,q):
    return c.levantamento(q)
