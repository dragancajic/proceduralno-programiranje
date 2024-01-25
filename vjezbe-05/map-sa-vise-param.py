#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:49:30 2024

@author: dragancajic
"""

# Slučaj kada funkcija `map` ima više argumenata

podaci = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
rezultat = list(map(round, podaci, range(1, 7)))
print(rezultat)  # [3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]


# пробајмо написати претходни кôд без употребе `map` функције:

rezultat = []
for broj in podaci:
    #rezultat.append(round(broj, 2))  # заокружи на 2 децимале
    #rezultat.append(float.__round__(broj, 3))
    # ili
    rezultat.append(round(broj, 3))
print(rezultat)  # [3.568, 5.577, 4.009, 56.242, 9.013, 32.0]
