#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:33:11 2024

@author: dragancajic
"""
# Zadatak 2

# Na programskom jeziku Python sastaviti funkciju koja pronalazi godine izbora
# u zvanje saradnika u nastavi i ispisuje ih na standardnom izlazu sortirane u
# opadajućem poretku. Npr.

# Milica, 2015
# Aleksa, 2019
# Jovan, 2017
# Vladimir, 2016

import re

def find_and_sort(filename):
    '''pronadji i sortiraj godine izbora u zvanje saradnika u nastavi'''
    with open(filename, encoding='utf-8') as file:
        text = file.read()
    pattern = re.compile(r"\d\d\d\d")
    #pattern = re.compile(r"[\d]{4}")
    years = pattern.findall(text)
    years.sort(reverse=True)
    return years

naziv_datoteke = input("Unesite naziv datoteke: ")
godine = find_and_sort(naziv_datoteke)
print("Godine izbora u zvanje:", ", ".join(godine))

# Da li se mogao napraviti kompaktniji regularni izraz? √

# output:
# Godine izbora u zvanje: 2019, 2017, 2016, 2015
