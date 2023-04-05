#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:25:20 2023

@author: dragancajic
"""

# sintaksa funkcije
def pozdrav(ime):
    """
    pozdravna poruka
    params: ime
    """
    print("Pozdrav, " + ime)


# poziv funkcije
pozdrav('Dragan')

print(pozdrav.__doc__)
