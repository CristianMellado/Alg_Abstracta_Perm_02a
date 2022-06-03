#Ejercicio 2a
#Se usan las funciones del anterior ejercicio
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

best_s = 10

desde = 3   # número de cifras
hasta = 5
primos = []

x = 10**(desde-1)    # 10**2 = 10**(3 cifras - 1) = 3 cifras,   10**4 = 10**(5 cifras - 1) = 5 cifras
while len(str(x)) <= hasta:
  x = GEN_PRIMO_SIGUIENTE(x + 1, best_s)
  if len(str(x)) <= hasta:
    primos.append(x)

anterior = primos[0]
for primo in primos:
  if len(str(primo)) > len(str(anterior)):
    print()
  print(primo, end=" ")
  anterior = primo

primos = []
bits = [16, 32, 64]

for bit in bits:
  parte = []
  while len(parte) < 10:
    primo = RANDOMGEN_PRIMOS(bit, best_s)
    if primo not in primos:
      parte.append(primo)
  primos.append(parte)

for i in range(len(bits)):
  print(bits[i], " bits: ", primos[i])

for fila in primos:
  print("Número de", len(bin(fila[0])) - 2, "bits")
