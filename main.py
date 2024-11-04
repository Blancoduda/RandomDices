""" Sorteador de dados """

import random

d1 = random.Random()
d2 = random.Random()

rolls = []
double = 0

for i in range (10):
  a = (random.randrange(1,7))
  b = (random.randrange(1,7))
  rolls.append((a,b))
  print(a,b)
  if a + b == 12:
    double = double +1
    print("Duplo seis!")
  i += 1
print(rolls)
print(double)