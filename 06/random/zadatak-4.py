#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:36:28 2024

@author: dragancajic
"""

# Zadatak 4 - `random` - Domaći

# Na slučajan način se generišu brojevi iz intervala [2, 15]. Generisanje se
# prekida kada se generiše broj koji se može predstaviti kao proizvod dva prosta
# broja. Ispitati da li je proizvod prostih faktora generisanih brojeva veći od
# sume složenih faktora brojeva koji se dobiju tako što se sve cifre generisanih
# brojeva nadopune do 9. Npr. generisani brojevi su [2, 8, 12, 9].
# Tražimo proste faktore brojeva [2, 8, 12, 9] i složene faktore brojeva
# [7, 1, 87, 0]. Smatramo da broj nula nema djelioca.

# kao prvo, potrebno je da generišemo listu;
# potrebno je da nađemo djelioce broja;
# potrebno je da provjerimo da li je broj prost ili nije;
# potrebno je da broju izmijenimo cifre tako sto ih nadopunimo do 9.

# sada ćemo pisati jednu po jednu funkciju

import random

def prost(n):
    broj_je_prost = True
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            broj_je_prost = False
            break
    return broj_je_prost

def djelioci_broja(n):
    lista = []
    for i in range(2, n+1):
        if n % i == 0:
            lista.append(i)
    return lista

# provjeravamo da li se broj može predstaviti kao proizvod dva prosta broja
def proizvod_dva_prosta(n):
    djelioci = djelioci_broja(n)
    # print("broj", n, "djelioci:", djelioci)
    if len(djelioci) > 3:
        return False
    if len(djelioci) == 3:
        if prost(djelioci[0]) and prost(djelioci[1]):
            return True
        else:
            return False
    if len(djelioci) == 2:
        return n == djelioci[0] ** 2
    # prethodni `if` smo mogli zamijeniti i sa:
    #   return prost(djelioci[0]) and prost(djelioci[1])

    # Preostaje slučaj kada je len(...) = 1, u tom slučaju je n prost broj.
    # Ne razmatramo djelioce manje od 2.
    # Postoji slučaj kada je djelioci = [], u tom slučaju je n = 1 ili 0.

    return False

def dopuni_cifre(n):
    cifre_broja = []

    if n == 0:
        cifre_broja = [0]

    while n > 0:
        c = n % 10
        n //= 10
        cifre_broja.insert(0, c)
    # imamo sve cifre broja, sada kreiramo dopunjene cifre do 9
    cifre_broja = [9-c for c in cifre_broja]

    novi_broj = 0
    for c in cifre_broja:
        novi_broj *= 10
        novi_broj += c
    return novi_broj

def generisi_listu(k, n):
    lista = []
    while True:
        gb = random.randint(k, n)
        lista.append(gb)
        if proizvod_dva_prosta(gb):
            break
    return lista

if __name__ == '__main__':
    lista = generisi_listu(2, 15)
    trazeni_proizvod = 1
    trazena_suma = 0

    for broj in lista:
        djelioci = djelioci_broja(broj)
        prosti_djelioci = [djelilac for djelilac in djelioci if prost(djelilac)]

        for pd in prosti_djelioci:
            trazeni_proizvod *= pd
        dopuna_9 = dopuni_cifre(broj)
        # print("broj =", broj)
        # print("prosti djelioci:", prosti_djelioci)
        djelioci = djelioci_broja(dopuna_9)
        slozeni_djelioci = [djelilac for djelilac in djelioci if not prost(djelilac)]
        # print("slozeni djelioci:", slozeni_djelioci)
        for sd in slozeni_djelioci:
            trazena_suma += sd
    print("generisana lista:", lista)
    print("trazena suma:", trazena_suma)
    print("trazeni proizvod:", trazeni_proizvod)

    if trazeni_proizvod > trazena_suma:
        print("Proizvod prostih faktora generisanih brojeva je veci od sume \
              slozenih faktora generisanih brojeva cije su cifre dopunjene do 9")
    else:
        print("Proizvod prostih faktora generisanih brojeva nije veci od sume \
              slozenih faktora generisanih brojeva cije su cifre dopunjene do 9")
