'''
Sa tastature se unosi prirodan broj n, a nakon toga se unose informacije
o n studenata, tj. unose se ime i prezime studenta i broj bodova koje je
student osvojio na ispitu. Za svakog unesenog studenta na ekran je potrebno
ispisati njegovo ime i prezime i ocjenu koju je dobio na ispitu.
'''
import sys

def izracunaj_ocjenu(broj_bodova):
    '''ocjena na ispitu'''
    kriterijum = {
        range(0, 51): 5,
        range(51, 61): 6,
        range(61, 71): 7,
        range(71, 81): 8,
        range(81, 91): 9,
        range(91, 101): 10
    }

    # for interval in kriterijum:
    #     if broj_bodova in interval:
    #         return kriterijum[interval]

    for interval, ocjena in kriterijum.items():
        if broj_bodova in interval:
            return ocjena

    return "Nije moguce izracunati ocjenu."


n = int(input("Unesite prirodan broj n (broj studenata): "))

if n < 1:
    sys.exit("n mora biti prirodan broj.")

ocjene = {}  # prazan rječnik <-- OK! √
for i in range(n):
    ime = input("Unesite ime i prezime studenta: ")
    bodovi = float(input("Unesite broj bodova: "))
    ocjena_na_ispitu = izracunaj_ocjenu(bodovi)
    ocjene[ime] = ocjena_na_ispitu

print()
print("-" * 50)
print("Rezultati ispita:")
print("-" * 50)
# for student in ocjene:
#     print(f"{student} : {ocjene[student]}")
#     print("-" * 50)

for student, ocjene in ocjene.items():
    print(f"{student} : {ocjene}")
    print("-" * 50)
