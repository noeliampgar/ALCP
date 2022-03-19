# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 22:25:23 2021

@author: Noelia Pérez Garcia-Consuegra, ALCP grupo 2, Informática-Matemáticas
"""

#Problema 1.5. La constante de Champernowne 
#es el numero irracional que se obtiene al concatenar
# los numeros naturales, del siguiente modo:
#0,1234567891011121314151617181920212223...
#Se puede ver que el digito en la posicion numero 
#12 despues del punto decimal es 1 (indicado en rojo
#arriba). Sea d_n el digito que ocupa el lugar n-esimo. Calcular
#d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000.

import math

def sacaDigitoPos(numero,posDigito): #saca el digito de "numero" en la posicion "posDigito" desde la menos significativa
    numero//=10**(posDigito-1)       
    return numero%10

def d(n):
    nDigGrupo=1                 	#numero de digitos de los numeros 1,2,..,9 (primer grupo)
    numsPorFila=1               	#si colocamos los numeros 1,2,..,9 en vertical hay 1 numero por fila, para 10..19,20..29,30..39,..,90..99 hay 10 por fila
    ultPos=9                    	#guardamos la posicion global del ultimo digito del grupo 1,2,..,9
    ultPosAnt=0                      
    nGrAnt=0                    	#cantidad de numeros hasta el grupo anterior inclusive (no digitos)
    while(n>ultPos):            	#si nuestra posicion buscada es mayor que 9 continuamos
        ultPosAnt=ultPos        	#guardamos la posicion global del ultimo digito del grupo anterior
        nGrAnt+=9*numsPorFila   	#nueva cantidad de numeros hasta el grupo anterior inclusive
        nDigGrupo+=1            	#numero de digitos de los numeros del nuevo grupo (para 10..19,20..29,30..39,..,90..99 es 2)
        numsPorFila=10**(nDigGrupo-1)
        ultPos+=9*numsPorFila*nDigGrupo
                                    #guardamos la posicion global del ultimo digito del nuevo grupo


    n=n-ultPosAnt               	#posicion que nos dan, pero relativa al grupo en el que estamos
    blokGr= math.ceil(n/nDigGrupo)  #de forma relativa al grupo, numero de bloque donde esta nuestra posicion
    modulo=(n-1)%nDigGrupo          #lo utilizo para conocer el digito exacto, conociendo el numero de bloque
    contieneDigito=nGrAnt+blokGr   	#bloque buscado (se trata de un numero de "nDigGrupo" digitos)
    return sacaDigitoPos(contieneDigito,nDigGrupo-modulo)  
              			         	#saco el digito exacto del bloque buscado 

def actividad1():                        
    return     d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)