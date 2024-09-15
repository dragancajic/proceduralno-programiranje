#                                           ---Funkcija map---

#Sintaksa: map(f, *iterables)
#Funkcija "f" se primjenjuje na svaki objekat u "iterables"

imenaMalaSlova = ["marko", "ana", "sara", "milos", "sanja"]

imenaVelikaSlova = list(map(str.upper, imenaMalaSlova))

print(imenaVelikaSlova)