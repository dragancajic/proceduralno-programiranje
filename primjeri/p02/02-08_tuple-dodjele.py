#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 03:36:48 2023

@author: dragancajic
"""

# `tuple` dodjele u `for` petljama

# Primjer 1

T = [(1, 2), (3, 4), (5, 6)]  # lista ntorki

for (a, b) in T:
    print(a, b)

print('~-' * 21)

# Primjer 2

D = {'a': 1, 'b': 2, 'c': 3}  # rjecnik
print(D.keys())
print(D.values())
print(D.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

print('~-' * 21)

for (key, value) in D.items():
    print(key, " => ", value)

print('~-' * 21)

# Primjer 3: nested sequence - листа као угнијежђена секвенца
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)
# 1 [2, 3] 4
# 5 [6, 7] 8
