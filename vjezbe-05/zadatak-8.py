#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:44:12 2024

@author: dragancajic
"""

# Zadatak 8

# Izračunati broj neparnih brojeva u listi koristeći `reduce`.

from functools import reduce
    
brojevi = [22, 12, 13, 32, 11, 44, 94, 78, 99]
rezultat = reduce(lambda broj_neparnih, broj:
                  broj_neparnih + 1
                      if broj % 2  # ако је непаран има остатак дијељења! -> True
                      else broj_neparnih,
                  brojevi,
                  0)  # иницијална вриједност

print (rezultat)  # 3


# РЈЕШЕЊЕ без употребе функције `reduce`
brojac = 0
for broj in brojevi:
    if broj % 2:  # broj % 2 != 0 <-- дакле, НЕПАРАН! `True`
        brojac = brojac + 1
    #print("tBrojac:", brojac)

print("Broj neparnih:", brojac)
