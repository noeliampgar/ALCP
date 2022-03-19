import sys
import time
import random
import signal

import actividad8 as act

def handler(signum, frame):
   raise Exception("out of time")

signal.signal(signal.SIGALRM, handler)

def pol_coef(a, i):
    if i >= len(a):
        return 0
    return a[i]

def pol_sumar(a, b, p):
    return [(pol_coef(a,i)+pol_coef(b,i))%p for i in range(max(len(a),len(b)))]

def pol_restar(a, b, p):
    return [(pol_coef(a,i)-pol_coef(b,i))%p for i in range(max(len(a),len(b)))]
    
def pol_multiplicar_escalar(a, k, p):
    return [(k*pol_coef(a,i))%p for i in range(len(a))]

def pol_multiplicar_escuela(a, b, p):
    c = []
    for i in range(len(b)):
        aux = pol_sumar(c[i:], pol_multiplicar_escalar(a, b[i], p), p)
        c = c[:i] + aux
    return c

def pol_multiplicar_karatsuba(a, b, p):
    n = len(a)
    m = len(b)
    if n < m:
        a, b = b, a
        n, m = m, n
    if m <= 10:
        prod = pol_multiplicar_escuela(a, b, p)
    elif m <= n//2:
        c0 = pol_multiplicar_karatsuba(a[:n//2], b, p)
        c1 = pol_multiplicar_karatsuba(a[n//2:], b, p)
        c1 = pol_sumar(c1, c0[n//2:], p)
        prod = c0[:n//2] + c1
    else:
        c0 = pol_multiplicar_karatsuba(a[:n//2], b[:n//2], p)
        c2 = pol_multiplicar_karatsuba(a[n//2:], b[n//2:], p)
        s1 = pol_sumar(a[:n//2], a[n//2:], p)
        s2 = pol_sumar(b[:n//2], b[n//2:], p)
        c1 = pol_multiplicar_karatsuba(s1, s2, p)
        s3 = pol_sumar(c0, c2, p)
        c1 = pol_restar(c1, s3, p)
        c1 = pol_sumar(c1, c0[n//2:], p)
        c2 = pol_sumar(c2, c1[n//2:], p)
        prod = c0[:n//2] + c1[:n//2] + c2
    return prod

# test1
p = 7
for d in range(200):
   f = [random.randint(0,p-1) for i in range(d)] + [random.randint(1,p-1)]
   g = [random.randint(0,p-1) for i in range(d)] + [random.randint(1,p-1)]
   h1 = pol_multiplicar_karatsuba(f,g,p)
   try:
      signal.alarm(2)
      h2 = act.mult_pol_mod(f,g,p)
      signal.alarm(0)
      if h1 != h2:
         print("test1: error!")
         print("mult_pol_mod(" + str(f) + ", " + str(g) + ", " + str(p) + ")")
         sys.exit(1)
   except Exception as e:
      print("test1: error!")
      print("exception: " + str(e))
      sys.exit(1)
print("test1: passed!")

# test2
p = 11
d = 10000
f = [random.randint(0,p-1) for i in range(d)] + [random.randint(1,p-1)]
g = [random.randint(0,p-1) for i in range(d)] + [random.randint(1,p-1)]
h1 = pol_multiplicar_karatsuba(f,g,p)
try:
   signal.alarm(5)
   h2 = act.mult_pol_mod(f,g,p)
   signal.alarm(0)
   if h1 != h2:
      print("test2: error!")
      print("mult_pol_mod(" + str(f) + ", " + str(g) + ", " + str(p) + ")")
      sys.exit(1)
except Exception as e:
   print("test2: error!")
   print("exception: " + str(e))
   sys.exit(1)
print("test2: passed!")

# test3
p = 13
for k in range(14):
   d = 2**k
   f = [random.randint(0,p-1) for i in range(d)]
   g = [random.randint(0,p-1) for i in range(d)]
   h1 = pol_multiplicar_karatsuba(f,g,p)
   h1 = [(pol_coef(h1,i)-pol_coef(h1,i+d))%p for i in range(d)]
   try:
      signal.alarm(5)
      h2 = act.mult_ss_mod(f,g,k,p)
      signal.alarm(0)
      if h1 != h2:
         print("test3 error!")
         print("mult_ss_mod(" + str(f) + ", " + str(g) + ", " + str(k) + ", " + str(p) + ")")
         sys.exit(1)
   except Exception as e:
      print("test3: error!")
      print("exception: " + str(e))
      sys.exit(1)   
print("test3: passed!")

# test4
p = 5
k = 20
d = 2**k
f = [1] * d
g = [p-1,0,1] + [0] * (d-3)
h1 = [p-2, p-2] + [0] * (d-2)
try:
   signal.alarm(500)
   h2 = act.mult_ss_mod(f,g,k,p)
   signal.alarm(0)
   if h1 != h2:
      print("test4 error!")
      print("mult_ss_mod((x^2^k-1)/(x-1), x^2-1, " + str(k) + ", " + str(p) + ")")
      sys.exit(1)
except Exception as e:
   print("test4: error!")
   print("exception: " + str(e))
   sys.exit(1)   
print("test4: passed!")
