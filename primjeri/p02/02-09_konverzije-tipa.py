#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 03:48:22 2023

@author: dragancajic
"""

print("Hello world")

T = ('cc', 'aa', 'dd', 'bb')

tmp = list(T)  # Make a list from a tuple's items
tmp.sort()     # SORT IN-PLACE (mutable operation!)
print(tmp)     # ['aa', 'bb', 'cc', 'dd']

T = tuple(tmp)
print(T)       # ('aa', 'bb', 'cc', 'dd')

T = ('cc', 'aa', 'dd', 'bb')
T = sorted(T)  # врати СОРТИРАНУ ЛИСТУ, од дате секвенце (аутоконверзија)
print(T)       # ['aa', 'bb', 'cc', 'dd']

# NAPOMENA: Nepromjenljivost sadržaja n-torki se odnosi na najviši nivo,
# ne i na unutrašnji sadržaj n-torke.
