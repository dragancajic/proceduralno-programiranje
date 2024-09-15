'''
Sa tastature se unose brojevi sve dok se ne unese 5 Armstrongovih
brojeva. Na ekran ispisati unesene Armstrongove brojeve.
'''

def armstrongov_broj(n):
    """
    Ispitaj da li je broj Armstrongov.
    """
    suma = 0
    n_kopija = n
    while n_kopija != 0:
        cifra = n_kopija % 10
        cifra **= 3
        suma += cifra
        n_kopija //= 10

    if suma == n:
        return True

    return False


BROJ_ARMSTRONGOVIH = 0
#N = 200
#N = 300
#N = 400
N = 500

for broj in range(1, N+1):
    if armstrongov_broj(broj):
        BROJ_ARMSTRONGOVIH += 1
        print(f"Broj {broj} je Armstrongov.")

if BROJ_ARMSTRONGOVIH < 5:
    print(f"Nema pet(5) Armstrongovih brojeva u [1,{N}]!")
else:
    print(f"U [1,{N}] ima {BROJ_ARMSTRONGOVIH} Armstrongovih brojeva.\nKRAJ")


# while BROJ_ARMSTRONGOVIH < 5:
#     broj = int(input("Unesite broj: "))

#     if armstrongov_broj(broj):
#         BROJ_ARMSTRONGOVIH += 1
#         print(f"Broj {broj} je Armstrongov.")

# print("Uneseno je 5 Armstrongovih brojeva.\nProgram se zavrsava...")
