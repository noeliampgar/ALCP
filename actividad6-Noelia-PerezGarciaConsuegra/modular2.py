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

def lista_de_bits(k):
   l = []
   while k > 0:
      l += [k%2]
      k //= 2
   return l

def potencia_mod(a, k, N):             # 0 <= a < N, k >= 0, N >= 2
   r = 1
   l = lista_de_bits(k)
   n = len(l)
   for i in range(n):
      r = multiplicar_mod(r, r, N)
      if l[n-1-i] == 1:
         r = multiplicar_mod(r, a, N)
   return r

