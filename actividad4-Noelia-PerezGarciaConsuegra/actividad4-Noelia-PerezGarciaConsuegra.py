# -*- coding: utf-8 -*-
"""
@author: Noelia Pérez Garcia-Consuegra, ALCP grupo 2, Informática-Matemáticas

Problema 4.4. Demostrar que es posible multiplicar dos matrices de
nxn con O(nlog_2 (7)) operaciones aritméticas. ¿Cuál es la cantidad de 
operaciones aritméticas si se las multiplica directamente haciendo los 
productos de filas con columnas?

La demostración de que la complejidad aritmética es O(n^log2(7)) la vimos 
en clase y no es necesario repetirla.

Respecto a la multiplicación usual de dos matrices A y B de dimensión 
nxn, tenemos que para cada fila de A realizamos n multiplicaciones 
(y n-1 sumas) para cada columna de B, por lo que para cada fila de A 
el número de operaciones está en O(nxn). Como hay n filas, el número 
total de operaciones está en O(n^3).

Ejemplos de matrices:
[[9,9,2,1,2,3,2,3],[2,1,3,4,22,1,4,6],[2,3,4,1,2,4,6,3],[8,2,1,3,5,3,2,1],[3,2,1,3,4,3,2,3],[3,2,5,7,3,2,1,4],[4,3,2,1,3,4,2,3],[3,2,1,3,4,3,2,3]]    
[[3,3,0,8,0,3,0,3],[0,8,3,4,00,8,4,6],[0,3,4,8,0,4,6,3],[B,0,8,3,5,3,0,8],[3,0,8,3,4,3,0,3],[3,0,5,7,3,0,8,4],[4,3,0,8,3,4,0,3],[3,0,8,3,4,3,0,3]]  
[[1,2,3],[4,5,6],[7,8,9]]
[[1,1,1],[1,1,1],[1,1,1]]
[[1,0,0],[0,1,0],[0,0,1]]
[[1,0],[0,1]]
[[1,2],[3,4]]
[[1,1],[1,1]]

"""
import random as rnd
import matplotlib.pyplot as plt
import time

def suma(A,B):
    n=len(A)
    C=[]
    for i in range(n):
        C.append([])
        for j in range (n):
            C[i].append(0)  
            C[i][j]=A[i][j]+B[i][j]            
    return C

def resta(A,B):
    n=len(A)
    C=[]
    for i in range(n):
        C.append([])
        for j in range (n):
            C[i].append(0)  
            C[i][j]=A[i][j]-B[i][j]            
    return C

def mult_strassen(A,B):
    n=len(A)
    if n == 1:
        return [[A[0][0]*B[0][0]]]
    esImpar=n%2!=0
    if(esImpar):
        for i in range (n):
            A[i]=A[i]+[0]
            B[i]=B[i]+[0]
        A=A+[[0]*(n+1)]
        B=B+[[0]*(n+1)]
    n+=1
   
    A11, A12, A21, A22, B11, B12, B21, B22= [], [], [], [], [], [], [], []
    for i in range((n//2)):
        A11 = A11 + [A[i][:(n//2)]]
        B11 = B11 + [B[i][:(n//2)]]
        
        A12 = A12 + [A[i][(n//2):]]
        B12 = B12 + [B[i][(n//2):]]
        
        A21 = A21 + [A[(n//2) + i][:(n//2)]]
        B21 = B21 + [B[(n//2) + i][:(n//2)]]
        
        A22 = A22 + [A[(n//2) + i][(n//2):]]
        B22 = B22 + [B[(n//2) + i][(n//2):]]
        
    M1=mult_strassen(suma(A11,A22),suma(B11,B22))
    M2=mult_strassen(suma(A21,A22),B11)
    M3=mult_strassen(A11,resta(B12,B22))
    M4=mult_strassen(A22,resta(B21,B11))
    M5=mult_strassen(suma(A11,A12),B22)
    M6=mult_strassen(resta(A21,A11),suma(B11,B12))
    M7=mult_strassen(resta(A12,A22),suma(B21,B22))
    
    C11=suma(resta(suma(M1,M4),M5),M7)
    C12=suma(M3,M5)
    C21=suma(M2,M4)
    C22=suma(suma(resta(M1,M2),M3),M6)

    C1, C2 = [], []
    for i in range((n//2)):
        C1 = C1 + [C11[i] + C12[i]]
        C2 = C2 + [C21[i] + C22[i]]
    C = C1 + C2

    if(esImpar):
        for i in range (n):
            C[i].pop()
        C.pop()
        
    return C

def tiempo():
    mindigs = 1
    maxdigs = 150
    digstep = 1
    
    numdigs = []
    tiempos = []
     
    n = mindigs
    while n <= maxdigs:
       A = []
       B = []
       for i in range(n):
           A.append([])
           B.append([])
           for j in range (n):
               A[i].append(rnd.randint(0,9))
               B[i].append(rnd.randint(0,9))


       ini = time.time()
       mult_strassen(A, B)
       fin = time.time()
       numdigs += [n]
       t = fin-ini
       tiempos += [t]
       n += digstep
    
    plt.plot(numdigs, tiempos, "m-")
    plt.grid(b=True, which='major',axis='both', color='g', linestyle='--', linewidth=0.7)
    plt.xlabel('dimensión matriz')
    plt.ylabel('tiempo [seg]')
    plt.savefig("mult_strassen.png")
    plt.show()
    plt.clf()