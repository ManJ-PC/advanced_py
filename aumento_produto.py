# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 20:31:46 2023

@author: jcruz
"""
class Aumento:
    def __init__(self, A):
        self._Perc = A
        
    def getAumento(self):
        return self._Perc
    
    def setAumento(self, A):
        self._Perc = A
        
        
class Produto:
    def __init__(self, N, Q, PU):
        self._Nome = N
        self._Quantidade = Q
        self._ValorUnitario = PU

    def CustoTotal(self):
        return self._Quantidade*self._ValorUnitario
    
    def CustoTotalAumento(self, Perc):
        return self._Quantidade * self._ValorUnitario *(1 + Perc/100)
    
    def ImprimeCabecalho(self):
        print(f"{'Nome':<10} {'Valor Unitário':>15} {'Quantidade':>15} {'Custo Total':>15} {'Custo Total com Aumento':>25}")
        
    def Imprime(self, A):
        print(f"{self._Nome:<10} {self._ValorUnitario:>15} {self._Quantidade:15.2f} {self.CustoTotal():15.2f} {self.CustoTotalAumento(A.getAumento()):25.2f}")

        
if __name__=='__main__':
    Produtos = []
    
    Produtos.append(Produto("LP1", 1, 10))
    Produtos.append(Produto("LP2", 2, 10))
    Produtos.append(Produto("LP3", 1.5, 15))
    
    Atualizacao = Aumento(float(input("Qual o valor do aumento: ")))
    
    CabecalhoImpresso = 0
    
    for P in Produtos:
        if CabecalhoImpresso == 0:
            P.ImprimeCabecalho()
            CabecalhoImpresso = 1
            
        P.Imprime(Atualizacao)