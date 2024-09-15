#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:43:02 2024

@author: dragancajic
"""

# LINEARNO PRETRAŽIVANJE koristimo kada želimo pronaći određeni element
# u nesortiranoj listi - (indeksi).

print(['d', 'a', 'b', 'a'].index('a'))  # 1
# Vraća индекс elementa koji se prvi pojavljuje u listi.

# Linearno pretraživanje počinje od indeksa 0 i prolazi kroz listu.


# U nastavku je par primjera linearnog pretraživanja.

# Primjer linearnog pretraživanja uz pomoć `while` petlje:

def linear_search_while(lst, value):
    i = 0
    while i != len(lst) and lst[i] != value:
        i = i + 1
    if i == len(lst):
        return -1
    else:
        return i


# Primjer linearnog pretraživanja uz pomoć `for` petlje:

def linear_search_for(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


# Stražarska linearna pretraga

# Dodat je jedan element u listu kako bismo izbjegli stalnu provjeru
# koja postoji kod pretrage korišćenjem `while` petlje. :thinking:

def linear_search(lst, value):
    i = 0
    while lst[i] != value:
        i = i + 1
    lst.pop()  # уклони посљедњи елемент из листе :thinking:
    if i == len(lst):
        return -1
    else:
        return i
