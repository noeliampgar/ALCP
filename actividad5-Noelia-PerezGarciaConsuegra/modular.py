def sumar_mod(a, b, N):          # 0 <= a,b < N, N >= 1
    c = a + b
    if c >= N:
        c -= N
    return c

def restar_mod(a, b, N):         # 0 <= a,b < N, N >= 1
    c = a - b
    if c < 0:
        c += N
    return c

def multiplicar_mod(a, b, N):    # 0 <= a,b < N, N >= 1
   c = a * b
   c %= N
   return c

def potencia_mod(a, k, N):             # 0 <= a < N, k >= 0, N >= 2
    if k == 0:                         # caso base (k = 0)
        r = 1                          # convencion: 0^0 = 1
    elif k % 2 == 0:                   # k es par (k > 0)
        r = potencia_mod(a, k//2, N)
        r = multiplicar_mod(r, r, N)
    else:                              # k es impar (k > 0)
        r = potencia_mod(a, k-1, N)
        r = multiplicar_mod(a, r, N)
    return r
