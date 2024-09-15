#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:44:56 2023

@author: dragancajic

~ Filter
"""

# funkcija koja filtrira samoglasnike
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    
    if variable in letters:
        return True
    else:
        return False

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']  # there are 2 x 'e'!

# filter funkcija
filtered = filter(fun, sequence)

print('The filtered letters are:')

for s in filtered:
    print(s)

# The filtered letters are:
# e
# e