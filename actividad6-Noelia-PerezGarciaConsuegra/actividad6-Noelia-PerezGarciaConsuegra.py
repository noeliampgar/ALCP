# -*- coding: utf-8 -*-
"""
@author: Noelia Pérez Garcia-Consuegra, ALCP grupo 2, Informática-Matemáticas

Deben resolver el problema 7.10 de las notas y subirlo aquí. Debe imprimirse 
una factorización no trivial del N dado.
Problema 7.10. Utilizar el método p - 1 de Pollard para factorizar
N = 1542201487980564464479858919567403438179217763219681634914787749213
utilizando B = 100. ¿Cómo se puede calcular gcd(a^beta-1,N) de forma eficiente?
"""

import math
import random   as rand
import modular2 as mod

def gcd_binario(x,y):    # (x,y) != (0,0)
    done=False
    d=1
    while not done:
        x = abs(x)
        y = abs(y)
        xespar = x%2 == 0
        yespar = y%2 == 0
        if x == 0:           # caso base: gcd(0,y)=y
            m = y
            done =True
        elif y == 0:         # caso base: gcd(x,0)=x
            m = x
            done=True
        elif xespar and yespar:
            d*=2
            x,y=x//2, y//2
        elif xespar:
            x//=2
        elif yespar:
            y//=2
        elif x > y:
            x,y=y, x-y
        else:
            x,y=x, y-x
    return d*m

# Criba de eratostenes
def cribaErat(n):
    criba=[0,0]+[1]*(n-1)
    for nat in range (2 , math.floor(math.sqrt(n))+1):
        if(criba[nat]==1):
            for i in range (2*nat,n+1,nat):
                criba[i]=0
    return criba


def beta(B):
    beta=1
    criba=cribaErat(B)
    for p in range(2,B+1):
        pAux=p
        if criba[p]:
            for i in range(math.ceil(math.log(N,p))):
                pAux*=p
            beta*=pAux
    return beta

# Metodo p-1 de Pollard, con B=100
def pollard(N,B):
    y=N
    # En caso de que y no produzca un factor no trivial, es decir, que y = N,
    # basta con repetir el experimento
    while  y==N or y==1:
        a=rand.randint(1,N-1)
        x=gcd_binario(a,N)
        if x !=1 :
            return x
        # aquí se calcula gcd(a^beta-1,N) de forma eficiente
        aBeta=mod.potencia_mod(a,beta(B),N)
        y=gcd_binario(aBeta-1,N)
    return y

# N y B del enunciado
N=1542201487980564464479858919567403438179217763219681634914787749213
B=100
factorA=pollard(N,B)
factorB=N//factorA
print ('N =',factorA,'*',factorB)