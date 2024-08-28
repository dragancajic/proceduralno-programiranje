'''
Sa tastature se unose cijeli brojevi sve dok se ne unese 0.
Na ekranu ispisati sumu unesenih brojeva.
'''
SUMA_1 = 0

while True:
    broj = int(input("Unesite broj: "))

    if broj == 0:
        break

    SUMA_1 += broj

print("Suma unesenih brojeva je:", SUMA_1)

print("\n---Drugi nacin---")

SUMA_2 = 0

broj = int(input("Unesite broj: "))

while broj != 0:
    SUMA_2 += broj
    broj = int(input("Unesite broj: "))

print("Suma unesenih brojeva je:", SUMA_2)
