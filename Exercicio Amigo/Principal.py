#from C_Pessoa import *
from C_Amigo import *
from C_Colega import *
if __name__=='__main__':
    A=Amigo('Rita', 936666145 ,'Porto',2022)
    C=Colega('Pedro',917675522 ,'Engenheiro', 'ISEP')
    print(A.LerNome(), A.LerTelef(), A. LerLocal(), A.LerAno())
    print(C.LerNome(), C.LerTelef(), C. LerProf(), C.LerLTrab())