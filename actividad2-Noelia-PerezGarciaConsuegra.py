# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:32:28 2021

@author: Noelia Pérez Garcia-Consuegra, ALCP grupo 2, Informática-Matemáticas
"""
def bolasEnCajas(n):
    
    #Configuración inicial: turno 0
    cajas=[1]*n
    turno=0
    posUltBola=0
    posTurno=0
    #Lo ejecuto hasta llegar a la configuración previa a la inicial
    while cajas[posUltBola] !=n:
        turno+=1
        while cajas[posUltBola]>0:
            posTurno+=1
            cajas[posUltBola]-=1
            cajas[(posUltBola+posTurno) % n]+=1
        posUltBola=(posUltBola + posTurno) % n
        posTurno=0

    #En el siguiente turno se repartirían las n bolas de una caja en las demás
    return turno+1