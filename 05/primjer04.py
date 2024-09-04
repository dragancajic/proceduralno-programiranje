"""
                    ---Rječnici---
"""

# Rječnik (engl. dictionary) je kolekcija podataka koja sadrži parove
# ključ-vrijednost.
# Ključevi u rječniku moraju biti jedinstveni i moraju biti nepromjenjivi
# objekti, poput nizova, brojeva ili tuplova.

# Vrijednosti u rječniku mogu biti bilo kakvi objekti:
# nizovi, brojevi, nizovi nizova, funkcije itd.

# Rječnici se koriste za mapiranje ključeva na vrijednosti
# i omogućavaju brz pristup podacima putem ključeva.

# rjecnik = dict()  # prazan rječnik

student = {
    "Ime": "Marko",
    "Prezime": "Markovic",
    "Godine": 20,
    "Indeks": "123/23"
}

print(student)

print("-" * 80)

print("Broj elemenata u rjecniku student:", len(student))
print()

# pristup elementima rječnika
print("Ime:", student["Ime"])
print()

# dodavanje novih elemenata u rječnik
student["Prosjek"] = 9.21
print("Student:", student)
print()

# ažuriranje vrijednost u rječniku
student["Indeks"] = "999/23"
print("Student (azirirano):", student)
print()

# brisanje elemenata iz rječnika
del student["Godine"]
print('Student (nakon "brisanja godina"):', student)
