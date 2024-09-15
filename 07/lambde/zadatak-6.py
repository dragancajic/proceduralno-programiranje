#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:04:59 2024

@author: dragancajic
"""

# Zadatak 6

# Data je lista listi. Napisati program koji ispisuje listu sa najmanjom i
# listu sa najvećom dužinom.

def max_duzina(lista):
    max_duzina_liste = max(len(x) for x in lista)
    max_lista = max(lista, key = lambda i: len(i))  # LOOK!
    return(max_duzina_liste, max_lista)  # <class 'tuple'>

def min_duzina(lista):
    min_duzina_liste = min(len(x) for x in lista)
    min_lista = min(lista, key = lambda i: len(i))  # LOOK!
    return(min_duzina_liste, min_lista)  # <class 'tuple'>

lista1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("Original lista:")
print(lista1)  # [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

print("\nLista sa maksimalnom duzinom:")
print(max_duzina(lista1))  # (3, [13, 15, 17])
print("\nLista sa minimalnom duzinom:")
print(min_duzina(lista1))  # (1, [0])
