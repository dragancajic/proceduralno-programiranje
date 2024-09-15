#Reduce funkcija je dio functools modula.
#Sintaksa: reduce(f, iterable[, initial]) gdje je:
    #"f": funkcija dva argumenta
    #iterable: iterabilni objekat (niz, lista, tuple itd.)
    #initial: opciona vrijednost prije procesa

from functools import reduce

brojevi = [10, 21, 13, 1, 2]

proizvod = reduce(lambda a, b: a*b, brojevi)
print(f"Proizvod brojeva {brojevi} : {proizvod}")

trostrukuProizvod = reduce(lambda a, b: a*b, brojevi, 3)
print(f"Trostruki proizvod brojeva {brojevi} : {trostrukuProizvod}")