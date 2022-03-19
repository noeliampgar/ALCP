# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:30:28 2021

@author: Noelia Pérez Garcia-Consuegra, ALCP grupo 2, Informática-Matemáticas


Calcular es_posible_ganar_con_n_piedras(10**6) en un tiempo menor a 10 s. 
Se aceptarán implementaciones que solo puedan calcular  
es_posible_ganar_con_n_piedras( n ) para valores de n mucho menores que 
10**6, digamos para 1<=n<=20, pero en ese caso solo les daré la mitad de 
la nota.
Problema 3.4. Considerar el siguiente juego de dos jugadores: partiendo de una pila de n piedras,
los jugadores van (uno tras otro) quitando 1, 2 o 6 piedras de la pila a su eleccion, hasta que el que
quita la ultima pierde. Implementar un algoritmo recursivo es_posible_ganar_con_n_piedras(n) que
determine si, partiendo de una pila de n piedras, hay estrategia ganadora.
"""
#Programacion dinámica que evita recursión por el agotamiento de la pila de recursión en python
#Utilizo una posición 0 para hacerlo más visual, ya que tabla[n] se corresponde con es_posible_ganar_con_n_piedras(n)
def es_posible_ganar_con_n_piedras(n):
    tabla=[False]*(n+1)
    tabla[0]=None
    tabla[1]=False #no es posible porque el único movimiento es quitar 1 piedra y, por tanto, perder
    j=2
    while j<=n:
        res=False
        for i in 1,2,6:
            if(j-i)>0: 
                res= not tabla[j-i]  #si el siguiente jugador parte de un juego imposible de ganar, éxito
                if(res):             #con encontrar una estrategia ganadora sirve, así que salgo del bucle
                    break
        tabla[j]=res                 #actualizo la tabla dinámica para j
        j+=1

    return tabla[n]



def prueba():
    for i in range (1,11):
        print (es_posible_ganar_con_n_piedras(i))



    