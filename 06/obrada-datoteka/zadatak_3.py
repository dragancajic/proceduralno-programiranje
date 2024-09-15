#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:22:22 2024

@author: dragancajic
"""

# Zadatak 3 | ПРЕЛИЈЕП ЗАДАТАК √ :sparkling_heart: :heartpulse: :gift_heart:

# U datoteci `brojevi1.txt` se nalaze prirodni brojevi, u svakom redu po jedan.
# Za svaki od brojeva koji se nalaze u datoteci čuvati LISTU SLOŽENIH BROJEVA
# koji ga dijele. Npr. u datoteci se nalaze brojevi 6, 32, 4, 2, 8, 5, pa je:
# za 6 se čuva [6]
# za 32 se čuva [4, 8, 16, 32]
# za 4 se čuva lista [4]
# za 2 se čuva prazna lista
# za 8 se čuva lista [4, 8]
# za 5 se čuva prazna lista.

# Koju metodu ćemo koristiti za čitanje sadržaja datoteke: `read`, `readline`
# ili `readlines`?
# Jasno da je od navedenih metoda najzgodnija metoda `readlines`, jer on čita
# sadržaj datoteke i čuva ga u listi, a elementi liste su SADRŽAJI LINIJA. :eyes:

#from typing import TextIO
#from io import StringIO

def slozeni_broj(n):
    '''
    Provjerava da li je broj n složen
    '''
    uslov = False
    for k in range(2, n):
        if n % k == 0:
            uslov = True
            break
    return uslov

def slozeni_djelioci(n):
    lista = []
    for k in range(2, n+1):  # zbog cega do n+1 ??? range() ИСКЉУЧУЈЕ ГОРЊУ ГРАНИЦУ!
        if n % k == 0 and slozeni_broj(k):
            lista.append(k)
    # lista = [k for k in range(2, n+1) if n % k == 0 and slozeni_broj(k)]
    # NICE! ГЕНИЈАЛНО! List Comprehension √ LOOK! :eyes:
    return lista

if __name__ == '__main__':
    # čitanje brojeva
    filename = "brojevi1.txt"
    with open(filename, 'r') as f:
        brojevi = f.readlines()
    # učitani brojevi su stringovi, iz tog razloga ih pretvaramo u integer-e! √
    brojevi = [int(broj) for broj in brojevi]

    d = dict()
    for k in brojevi:
        d[k] = slozeni_djelioci(k)
    print("trazeni rezultat je:")
    print(d)
