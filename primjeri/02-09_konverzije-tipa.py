#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 03:48:22 2023

@author: dragancajic
"""

print("Hello world")

T = ('cc', 'aa', 'dd', 'bb')

tmp = list(T)  # Make a list from a tuple's items
tmp.sort()
print(tmp)

T = tuple(tmp)
print(T)

T = ('cc', 'aa', 'dd', 'bb')
T = sorted(T)
print(T)

# NAPOMENA: Nepromjenljivost sadrzaja n-torki se odnosi na najvisi nivo,
# ne i na unutrasnji sadrzaj n-torke.
