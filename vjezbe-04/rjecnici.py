#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 06:25:49 2024

@author: dragancajic
"""

# ~ Rječnici ~

# Sintaksa definisanja rječnika je:
# imeRjecnika = {kljuc1 : vrijednost1, kljuc2 : vrijednost2, kljuc3 : vrijednost3, ...}

# Ako se želi definisati prazan rječnik, to se radi na način:
imeRjecnika = {}  # или овако: `prazan_rjecnik = dict()`

rjecnik = {
    1: "Januar",
    2: "Februar",
    3: "Mart",
    4: "April",
    5: "Maj",
    6: "Jun",
    7: "Jul",
    8: "Avgust",
    9: "Septembar",
    10: "Oktobar",
    11: "Novembar",
    12: "Decembar"
}

print(rjecnik[2])  # Februar
print(rjecnik[6])  # Jun

list_of_tuples = rjecnik.items()  # <class 'dict_items'>
print(list_of_tuples, "\n")
'''
output:
# dict_items([
    (1, 'Januar'),
    (2, 'Februar'),
    (3, 'Mart'),
    (4, 'April'),
    (5, 'Maj'),
    (6, 'Jun'),
    (7, 'Jul'),
    (8, 'Avgust'),
    (9, 'Septembar'),
    (10, 'Oktobar'),
    (11, 'Novembar'),
    (12, 'Decembar')
])
'''

for item in list_of_tuples:
    print(type(item), item)

print(len(list_of_tuples))  # 12 √


lista_kljuceva = rjecnik.keys()

print(lista_kljuceva, "|", type(lista_kljuceva))
# dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) | <class 'dict_keys'>

print(len(lista_kljuceva)) # 12 √

rjecnik.update({7 : "Mjesec Jul"})

lista_vrijednosti = rjecnik.values()

print(lista_vrijednosti)  # <class 'dict_values'>
# dict_values(['Januar', 'Februar', 'Mart', 'April', 'Maj', 'Jun', 'Mjesec Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar'])

print(len(lista_vrijednosti))  # 12 √
