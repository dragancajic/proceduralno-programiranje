'''
                            ---Deklaracija promjenljive---

Identifikatori su imena koja koristimo da bismo odredili (identifikovali) različite
elemente programa.
Identifikatori mogu da se sastoje od slova (malih i velikih), cifara i znaka “_“,
ali nije dozvoljeno da počinju cifrom.

Primjeri pravilne upotrebe identifikatora:
    x
    Y
    slovo
    Slovo
    SLOVO
    vrijednost_10
    brojSamoglasnika

Primjeri nepravilne upotrebe identifikatora:
    1broj
    “rijec”
    ab-cd

Promjenljive su osnovni objekti koje koristimo u programiranju.
Svakoj promjenljivoj je pridružen određen memorijski prostor koji služi za čuvanje
odgovarajućeg podatka, koji predstavlja vrijednost promjenljive.

Promjenljive su identifikatori, što znači da za određivanje naziva promjenljive važe
opšta pravila koja važe i za identifikatore.

Korištenje promjenljivih podrazumjeva deklaraciju same promjenljive, dodjelu vrijednosti,
eventualne kasnije izmjene vrijednosti, kao i upotrebu dodijeljene vrijednosti.

Deklarisanje promenljivih u Pajtonu se sastoji iz imena promjenljive (identifikatora)
poslije čega slijedi operator dodjele (=), a zatim slijedi inicijalna vrijednost.
'''

x = 3
X = 15  # case-sensitive
Y = 2.8
BROJ_SAMOGLASNIKA = 5
brojSuglasnika = 25

print("x =", x)
print("X =", X)
print("Y =", Y)
print("Broj samoglasnika:", BROJ_SAMOGLASNIKA)
print("Broj suglasnika:", brojSuglasnika)

print("-----------------------------")
x = 10
print("x =", x)

print("-----------------------------")
a, b, c = 3, 10, 20

print("a =", a)
print("b =", b)
print("c =", c)
