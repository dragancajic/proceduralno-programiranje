'''
                    ---Iteracija kroz rječnik---
'''

bodovi = {
    "Marko Markovic": 92,
    "Milos Milosevic": 76,
    "Ana Anic": 87,
    "Sara Saric": 91,
    "Petar Petrovic": 52
}

# ispis ključeva
print("Kljucevi:")
for kljuc in bodovi.keys():
    print("\t", kljuc)
print()

# ispis vrijednosti
print("Vrijednosti:")
for vrijednost in bodovi.values():
    print("\t", vrijednost)
print()

# ključ-vrijednost u paru
print("Parovi kljuc: vrijednost (prvi nacin):")
for kljuc, vrijednost in bodovi.items():
    print(f"\t{kljuc:15}: {vrijednost}")
print()

print("Parovi kljuc: vrijednost (drugi nacin):")
for kljuc in bodovi:
    print(f"\t{kljuc:15}: {bodovi[kljuc]}")

# više o metodama rječnika možete pronaći na:
# https://www.w3schools.com/python/python_ref_dictionary.asp
