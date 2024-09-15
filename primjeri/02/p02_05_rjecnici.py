#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:09:20 2023

@author: dragancajic
"""

mapa = {"ime": "Dragan", "prezime": "Cajic"}

print(mapa.keys())
print(mapa.values())
print(mapa.items())

for key, value in mapa.items():
    print(f"kljuc: {key}, vrijednost: {value}")
