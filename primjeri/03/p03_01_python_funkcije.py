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


# primjer:

def f(x, y):
    z = 2 * (x + y)
    return z


print("Program starts!")
a = 3
res1 = f(a, 2+a)
print("Result of function call:", res1)  # f(3, 2+3) -> 16

a = 4
b = 7
res2 = f(a, b)
print("Result of function call:", res2)  # f(4, 7) -> 22
