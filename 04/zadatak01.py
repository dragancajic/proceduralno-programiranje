'''
Sa tastature se unosi prirodan broj n, a nakon toga još n brojeva.
Na ekran ispisati najmanji od unesenih brojeva.
'''
import sys

n = int(input("Unesite prirodan broj n: "))

if n <= 0:
    sys.exit("n mora biti prirodan broj")

najmanji = float("inf")


# prvi (1.) način

for i in range(n):
    broj = int(input("Unesite broj sa tastature: "))

    if broj < najmanji:
        najmanji = broj

print("Najmanji od unesenih brojeva:", najmanji)

print("-" * 50)


# drugi (2.) način

L = []

for i in range(n):
    # broj = int(input("Unesite broj sa tastature: "))
    # L.append(broj)
    L.append(int(input("Unesite broj sa tastature: ")))

print("Najmanji od unesenih brojeva:", min(L))
