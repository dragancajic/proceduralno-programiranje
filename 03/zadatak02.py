'''
Za prirodan broj n kažemo da je Armstrongov ako je n jednak
sumi kubova njegovih cifara.

Na primjer, broj 153 je Armstrongov jer je
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

Napisati program koji za prirodan broj koji se unosi sa tastature
ispituje da li je Armstrongov.
'''
import sys

n = int(input("Unesite prirodan broj n: "))

if n <= 0:
    sys.exit("n mora biti prirodan broj!")

SUMA = 0
nKopija = n
while nKopija != 0:
    cifra = nKopija % 10  # 153 % 10 = 3, 15 % 10 = 5, 1 % 10 = 1
    cifra **= 3     # 3^3 = 27, 5^3 = 125, 1^3 = 1
    SUMA += cifra   # 0 + 27 = 27, 27 + 125 = 152, 152 + 1 = 153
    nKopija //= 10  # 153 // 10 = 15, 15 // 10 = 1, 1 // 10 = 0

if SUMA == n:
    print(f"Broj {n} je Armstrongov broj.")
else:
    print(f"Broj {n} nije Armstrongov broj.")
