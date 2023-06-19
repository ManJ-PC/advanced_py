# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:14:40 2023

@author: jcruz
"""

import math
class Temperatura():    
    def __init__(self, C):
        self._C = C
        self._F = 1.8*C+32
        
    def getFahrenheit(self):
        return self._F
    
    def setFahrenheit(self, F):
        self._F=F
        self._C = (F - 32)/1.8
    
    def getCelsius(self):
        return self._C
    
    def setCelsius(self, C):
        self._C = C
        self._F = 1.8*C+32
        
    def Imprime(self):
        print(f"{self._F:5.3} graus Fahernheit correspondem a {self._C:5.3} graus Celsius.")

if __name__=='__main__':
    T=Temperatura(float(input("Qual a temperatura em graus Celsius: ")))
    T.Imprime()
    
    T.setFahrenheit(float(input("Qual a temperatura em graus Fahernheit: ")))
    T.Imprime()
               
    T.setCelsius(float(input("Qual a temperatura em graus Celsius: ")))
    T.Imprime()
