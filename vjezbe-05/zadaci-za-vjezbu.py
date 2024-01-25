#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:09:12 2024

@author: dragancajic
"""

# Zadaci za vježbu

# 1. Koristeći `map` funkciju ispisati kvadrat svakog broja iz date liste
# zaokruzen na tri decimale.

lista = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

kvadrat = list(map(lambda x: round(x * x, 3), lista))
print(kvadrat)  # [18.922, 37.088, 10.562, 95.453, 4.666, 78.854, 21.068]

# 2. Koristeći `filter` funkciju ispisati imena, iz date liste, koja sadrže
# manje od 7 slova.

imena = ["Milica", "Anastasija", "Danijela", "Nikolina", "Ana"]

imena7 = list(filter(lambda ime: len(ime) < 7, imena))
print(imena7)  # ['Milica', 'Ana']

# 3. Koristeći `reduce` funkciju ispisati proizvode brojeva iz liste.

from functools import reduce

brojevi = [4, 6, 9, 23, 5]

proizvod = reduce(lambda x, y: x * y, brojevi)
print(proizvod)        # ((((4 * 6) * 9) * 23) * 5) = 24840
print(type(proizvod))  # <class 'int'>
