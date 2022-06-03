# Ejercicio 1a
def EXPMOD(a, x, n):
  c = a % n
  r = 1
  while (x > 0):
    if x % 2 != 0:
      r = (r * c) % n
    c = (c * c) % n
    x = int(x/2)
  return r
  
EXPMOD(2,1000,13)

def EXPMOD(a,x,n):
  if x==0:
    return 1
  elif x%2==0:
    return (EXPMOD(a,x/2,n)**2) % n
  else:
    return ((a % n)*EXPMOD(a,x-1,n)) % n
    
EXPMOD(2,1000,13)

import random

def ES_COMPUESTO(a, n, t, u):
  x = EXPMOD(a,u,n)
  if x == 1 or x == n-1:
    return False  # n puede q sea primo
  for i in range(t):
    x = EXPMOD(x,2,n)
    if x == n-1:
      return False  # n puede q sea primo
  return True    # n es un número compuesto

def gen_random_a(n, s):  # genera "s" numeros random unicos en el rango de 2 y n-1, si no se pueden generar "s" números entonces retorna lo que tenga
  randoms = []
  maximo = min(s, n-3)
  while len(randoms) < maximo:
    num = random.randint(2, n-1)
    if num not in randoms:
      randoms.append(num)
  return randoms

def MILLER_RABIN(n, s):
  t = 0
  u = n - 1
  while u % 2 == 0:
    u = u//2
    t = t + 1
  for a in gen_random_a(n, s):
    if ES_COMPUESTO(a, n, t, u):
      return False
  return True

MILLER_RABIN(41, 10)

def RANDOMBITS(b):
  n = random.randint(0, 2**b - 1)
  m = 2**(b-1) + 1
  return n | m    # "|" para hacer una operación binaria de "n" y "m" en binario(bin(n) o bin(m)).

def RANDOMGEN_PRIMOS(b, s):
  n = RANDOMBITS(b)
  while MILLER_RABIN(n, s) == False:
    n = n + 2
  return n

def GEN_PRIMO_SIGUIENTE(n, s):
  n = n + 1 - (n % 2)
  while MILLER_RABIN(n, s) == False:
    n = n + 2
  return n

GEN_PRIMO_SIGUIENTE(1013 + 1, 100)

GEN_PRIMO_SIGUIENTE(14071 + 1, 100)

for i in range(2, 14081):
  if 14081%i==0: # comprobamos que es primo viendo si del 2 a 14080 es divisible.
    print("14081 No es primo")
    
# no imprime que no es primo, por ende es primo.

numero_pruebas = 100

for s in range(0, 101):
  print("s: ", s, end="")

  r = 0
  primos = []

  while len(primos) < numero_pruebas:
    primo = RANDOMGEN_PRIMOS(random.randint(4,64), s)
    if primo not in primos:
      primos.append(primo)

  for primp in primos:
    if MILLER_RABIN(primo, 100):
      r += 1
  print(" aprobados: ", r/numero_pruebas)
