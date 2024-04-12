'''
Sa tastature se unose cijeli brojevi sve dok se ne unese 0.
Na ekranu ispisati sumu unesenih brojeva.
'''
suma = 0

while (True):
    broj = int(input("Unesite broj: "))

    if (broj == 0):
        break

    suma += broj

print("Suma unesenih brojeva je:", suma)

print("\n---Drugi nacin---")

suma = 0

broj = int(input("Unesite broj: "))

while(broj != 0):
    suma += broj
    broj = int(input("Unesite broj: "))

print("Suma unesenih brojeva je:", suma)
