# -*- coding: utf-8 -*-
"""
@author: Noelia Pérez Garcia-Consuegra, ALCP grupo 2, Informática-Matemáticas

Se espera un fichero "actividad8.py" que implemente las funciones 
mult_pol_mod(f,g,p) y mult_ss_mod(f,g,k,p).

La función mult_pol_mod(f,g,p) debe calcular el producto de los 
polinomios f y g en el anillo (Z/pZ)[x], donde f, g, y el resultado 
están representados por la lista sus coeficientes (enteros entre 0 y p-1), 
empezando por el término independiente. 
Por ejemplo, la llamada mult_pol_mod([1,2,3], [4,5], 7) debe devolver [4,6,1,1], 
ya que (1+2x+3x^2)*(4+5x)=4+6x+x^2+x^3 en (Z/7Z)[x].

La función mult_ss_mod(f,g,k,p) debe calcular el producto de los polinomios 
f y g en el anillo (Z/pZ)[x]/<x^2^k+1>, donde f, g, y el resultado están 
representados por la lista sus 2^k coeficientes (enteros entre 0 y p-1), 
empezando por el término independiente. En esta función, las listas que 
representan f, g, y el resultado son de longitud exactamente 2^k. 
Por ejemplo, la llamada mult_ss_mod([1,2,3,4], [4,5,6,6], 2, 7) deberá devolver 
[3,6,4,0], ya que (1+2x+3x^2+4x^3)*(4+5x+6x^2+6x^3)=3+6x+4x^2 en (Z/7Z)[x]/<x^4+1>. 
Esta función debe implementar el método de Schonhage-Strassen de forma recursiva
 con casos bases k=0,1,2.
 
"""


# Multiplica f(x) * x^pot y reduce mod <x^t+1> en Zp
def potred(f, pot, t, p):
    if pot == 0:
        return f
    ret = [0]*t
    if pot <= len(f):
        sign=1
    else:
        sign=-1
    for i in range(len(f)):
        if (i+pot) % t == 0:
            sign = -sign         
        ret[(i+pot) % t] = (ret[(i+pot) % t] + sign * f[i]) % p
    return ret


# DFT(f) (modificación Cooley-Tuckey) con f lista de lista
def dft(f, xi, p):
    n = len(f)
    n1 = len(f[0])  # longitud coeficientes
    if n == 1:
        return f
    f_even = [[0]*n1] * (n//2)
    f_odd = [[0]*n1] * (n//2)
    for i in range(n//2):
        f_even[i] = f[2*i]
        f_odd[i] = f[2*i+1]
    a_even = dft(f_even, xi*2, p)
    a_odd = dft(f_odd, xi*2, p)
    a = [[0]*n1] * n
    for i in range(n//2):
        aux2 = potred(a_odd[i], xi*i, n1, p)
        a[i] = [(a_even[i][j] + aux2[j]) % p
                for j in range(n1)] 
        a[i+n//2] = [(a_even[i][j] - aux2[j]) % p
                      for j in range(n1)]
    return a


# transformada inversa
def invDft(a, xi, p):
    n2 = len(a)
    n1 = len(a[0])
    res = dft(a, 2*n1-xi, p)
    inv = pow(n2, -1, p)
    for i in range(n2):
        for j in range(n1):
            res[i][j] = (res[i][j] * inv) % p
    return res


# negaconvolucion
def negaconvolucion(fPrima, gPrima, k1, k2, p):
    n1 = pow(2, k1)
    n2 = pow(2, k2)
    xi = (2*n1)//n2
    expA = [xi*i for i in range(n2)]
    af2 = [potred(fPrima[i], expA[i], 2*n1, p) for i in range(n2)]
    ag2 = [potred(gPrima[i], expA[i], 2*n1, p) for i in range(n2)]
    dft1 = dft(af2, xi*2, p)
    dft2 = dft(ag2, xi*2, p)
    prod = [mult_ss_mod(dft1[i], dft2[i], k1+1, p) for i in range(n2)]
    inv_dft = invDft(prod, xi*2, p)
    expA_inv = [2*n2*xi - xi*i for i in range(n2)]
    hPrima = [potred(inv_dft[i], expA_inv[i], 2*n1, p)
                for i in range(n2)]
    return hPrima


# producto de dos polinomios (Schönhage-Strassen)
def mult_ss_mod(f, g, k, p):
    k1 = k // 2
    k2 = k - k1
    n1 = pow(2, k1)
    n2 = pow(2, k2)
    if k == 0:
        return [f[0] * g[0] % p]
    elif k == 1:
        return [(f[0] * g[0] - f[1] * g[1]) % p, (f[0] * g[1] + f[1] * g[0]) % p]
    elif k == 2:
        return [(f[0] * g[0] - f[1] * g[3] - f[2] * g[2] - f[3] * g[1]) % p,(f[0] * g[1] + f[1] * g[0] - f[2] * g[3] - f[3] * g[2]) % p,
                (f[0] * g[2] + f[1] * g[1] + f[2] * g[0] - f[3] * g[3]) % p,(f[0] * g[3] + f[1] * g[2] + f[2] * g[1] + f[3] * g[0]) % p]
    fPrima = [[f[j]
                for j in range(i*n1, (i+1)*n1)] + ([0]*n1) for i in range(n2)]
    gPrima = [[g[j]
                for j in range(i*n1, (i+1)*n1)] + ([0]*n1) for i in range(n2)]
    hPrima = negaconvolucion(fPrima, gPrima, k1, k2, p)
    h = [(x-y) % p for (x, y) in zip(hPrima[0][:n1], hPrima[n2-1][n1:])]
    for i in range(1, n2):
        h += [(x+y) % p for (x, y) in zip(hPrima[i-1][n1:], hPrima[i][:n1])]
    return h


# Producto de dos polinomios f y g en Zp[x]
def mult_pol_mod(f, g, p):
    n = len(f)
    m = len(g)
    if n == 0 or m == 0:
        return []
    gradof = n-1
    gradog = m-1
    x = 1
    k = 0
    while x <= gradof + gradog:
        x *= 2
        k += 1
    f += [0]*(pow(2, k) - n)
    g += [0]*(pow(2, k) - m)
    h = mult_ss_mod(f, g, k, p)   
    while h and h[-1] == 0:
        h.pop()
    return h