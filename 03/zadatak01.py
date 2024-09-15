'''
Sa tastature se unosi prirodan broj n.
Napisati program koji na ekran ispisuje vrijednost n!.
'''
import sys

n = int(input("Unesite prirodan broj n: "))

if n <= 0:
    sys.exit("n mora biti prirodan broj!")

FAKTORIJEL = 1

for i in range(2, n+1):
    FAKTORIJEL *= i

print(f"{n}! = {FAKTORIJEL}")
