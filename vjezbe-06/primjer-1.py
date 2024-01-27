#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:46:18 2024

@author: dragancajic
"""

# Modul `math` - obrađeno kroz prethodne vježbe.
# ~- ~- ~- ~- ~- ~- ~- ~- ~- ~- ~- ~- ~- ~- ~- ~
# `random` - par jednostavnijih primjera:

# Primjer 1 - nasumično ispisati imena u listi

import random

ime = ["Milica", "Marija", "Marko", "Ana"]

for i in range(1, 5):
    random_ime = random.choice(ime)
    print(random_ime)
    ime.remove(random_ime)

#print(ime)       # []
#print(len(ime))  # 0
