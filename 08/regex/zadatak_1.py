#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:58:12 2024

@author: dragancajic
"""

# Zadatak 1

# Na programskom jeziku Python sastaviti program koji ispisuje pozicije
# pojavljivanja riječi u tekstu.

# Unesite tekst: nebo je plavo, trava je zelena
# Unesite reč za pretragu: je

# Riječ se javlja na poziciji 5
# Riječ se javlja na poziciji 21

import re

text = input("Unesite tekst: ")
pattern = re.compile(input("Unesite riječ za pretragu: "))

for match in pattern.finditer(text):
    print("Riječ se javlja na poziciji: {}".format(match.start()))


# output:
# Riječ se javlja na poziciji: 5
# Riječ se javlja na poziciji: 21
