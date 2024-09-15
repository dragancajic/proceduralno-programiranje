#                                           ---Moduo random---

import random

#random.randint(a, b) - slucajno generisanje cijelog broja iz intervala [a, b]
print("Slucajno generisan cijeli broj iz intervala [10, 20]:", random.randint(10, 20))
print()

#random.random() - generisanje slucajnog broja iz intervala [0, 1)
print("Slucajan broj iz intervala [0, 1):", random.random())
print()

#random.choice(kolekcija) - vraca slucajno odabran element iz neke kolekcije
voce = ["Jabuka", "Banana", "Kruska", "Kivi", "Mandarina"]
print("Slucajno odabrano voce:", random.choice(voce))
print()

#random.shuffle(kolekcija) - permutuje elemente kolekcije na slucajan nacin
random.shuffle(voce)
print("Voce nakon permutovanja:", voce)