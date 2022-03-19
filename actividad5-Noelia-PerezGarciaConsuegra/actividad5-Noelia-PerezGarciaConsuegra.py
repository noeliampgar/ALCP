# -*- coding: utf-8 -*-
"""
@author: Noelia Pérez Garcia-Consuegra, ALCP grupo 2, Informática-Matemáticas
"""
'''
Un entero N >= 2 se dice pseudoprimo si para cualquier entero a coprimo con N se
cumple que a_(N-1) = 1 (mod N). El teorema de Euler-Fermat muestra que todo primo es pseudoprimo,
pero lamentablemente la recíproca no es cierta. Escribir un programa en Python3 que determine 
los 10 menores pseudoprimos que no son primos.
'''
import modular as mod
import math

def es_primo(n):
	if n == 2 or n == 3:
		return True
	if n% 2 == 0 or n % 3 == 0:
		return False
	else:
		k = 1
		while (6*k - 1)**2 <= n:
			if n%(6*k + 1 ) == 0 or n%(6*k - 1) ==0:
				return False
			k +=1
		return True

#función que decide si un numero n es pseudoprimo pero no primo
def esPseudoNP(n):
    if es_primo(n):
        return False
    for coprimo in range(2,n):
        if math.gcd(coprimo,n)==1:
            if mod.potencia_mod(coprimo,n-1,n)!=1:
                return False
    return True

# n menores pseudoprimos no primos
def fun(n):
    pseudo=[];
    i=4
    while len(pseudo)<n:
        if esPseudoNP(i):
            pseudo+=[i]
        i+=1
    return pseudo

# 10 menores pseudoprimos no primos
print(fun(10))