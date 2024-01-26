#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 20:58:08 2024

@author: dragancajic
"""

# Zadatak 4

# Napisati program koji obrće redoslijed slova u listi stringova.

'''Program koji obrće redoslijed slova u listi stringova.'''

def obrni_slova_niski_liste(lista_niski):
    lista_obrnutih_slova = list(map(lambda niska: "".join(reversed(niska)), lista_niski))
    return lista_obrnutih_slova

boje = ["Crvena", "Zelena", "Plava", "Bijela", "Crna"]
print("Original lista niski:")
print(boje)
print("\nObrnute rijeci liste:")
print(obrni_slova_niski_liste(boje))
"""
output:

Original lista niski:
['Crvena', 'Zelena', 'Plava', 'Bijela', 'Crna']

Obrnute rijeci liste:
['anevrC', 'aneleZ', 'avalP', 'alejiB', 'anrC']
"""
