'''
Napisati program koji sabira argumente komandne linije.
'''

import sys

n = len(sys.argv)
print("Ukupan broj argumenata:", n)

print("Naziv programa:", sys.argv[0])

print("\nProsljedjeni argumenti:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

SUMA = 0
for i in range(1, n):
    SUMA += float(sys.argv[i])

print("\nSuma argumenata:", SUMA)

# Pokretanje:
# python primjer07.py 2.51 3.14 2.30

# izlaz:
# Ukupan broj argumenata: 4
# Naziv programa: primjer07.py

# Prosljedjeni argumenti: 2.51 3.14 2.30
# Suma argumenata: 7.95
