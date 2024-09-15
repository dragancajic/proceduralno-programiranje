#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:45:42 2024

@author: dragancajic
"""

# Primjer 2

import random

lista = ["jabuka", "banana", "visnja"]
print(random.choices(lista, weights = [10, 1, 1], k = 14))

random_voce = random.choices(lista, weights = [10, 1, 1], k = 14)
random_voce = random.choices(lista, weights = [10, 1, 1], k = 14)
ispis_voce = list(map(lambda voce: voce, random_voce))

for v in ispis_voce:
    print(v)

# `weights` - 10 puta je veća vjerovatnoća da će se ispisati `jabuka`
# nego druga dva elementa liste! <-- LOOK! :eyes:
