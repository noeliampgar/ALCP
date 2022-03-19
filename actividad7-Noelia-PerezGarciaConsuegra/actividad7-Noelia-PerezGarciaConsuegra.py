# -*- coding: utf-8 -*-
"""

@author: Noelia Pérez Garcia-Consuegra, ALCP grupo 2, Informática-Matemáticas

"""
import modular2 as m2
import random as rand
import matplotlib.pyplot as plot


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

# Programa de Jacobi
def jacobi(a, n):
    a %= n
    val = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                val = -val
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            val = -val
        a %= n
    if n == 1:
        return val
    else:
        return 0


# k veces el test de primalidad de Solovay-Strassen 
def generar_primo(n,k):
    cnt=0
    primoEnc=False
    while not primoEnc:
        N=rand.randint(10**(n-1),10**n-1)
        #Condiciones Solovay-Strassen
        if N%2!=0 and N>=3: 
            i=0
            while i<k:
                a=rand.randint(1,N-1)
                if gcd_binario(a,N)!=1:
                    break
                jac=jacobi(a,N)
                pot=m2.potencia_mod(a,(N-1)//2,N)
                if m2.restar_mod(jac,pot,N)!=0:
                    break
                i+=1
            cnt+=1
            primoEnc= i==k
    p=N   
    return (p,cnt)

def generar_histograma():
    cntL=[]
    for i in range (50):
        p,cnt=generar_primo(300,20)
        cntL+=[cnt]
    intervalos = range(min(cntL), max(cntL) + 210,100) #calculamos los extremos de los intervalos
   
    plot.hist(x=cntL, bins=intervalos, color='#F2AB6D', rwidth=0.85)
    plot.title('Histograma de intentos')
    plot.xlabel('intentos')
    plot.ylabel('Frecuencia')
    plot.xticks(intervalos)
    plot.savefig("histograma.png")
    plot.show()  
    
