#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 03:36:48 2023

@author: dragancajic
"""

# tuple dodjele u for petljama
T = [(1, 2), (3, 4), (5, 6)]

for (a, b) in T:
    print(a, b)


D = {'a': 1, 'b': 2, 'c': 3}

for (key, value) in D.items():
    print(key, " => ", value)


# nested sequence
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)
