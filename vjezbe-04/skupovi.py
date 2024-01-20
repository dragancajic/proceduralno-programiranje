#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:51:48 2024

@author: dragancajic
"""

# ~ Sets - skupovi ~

# Promjenljiva, neuređena, neindeksirana struktura zasnovana na heš mapama. √
# Defisana (sa) vitičastim zagradama (bez ključa, za razliku od heš-mapa).  √

# Inicijalizacija:
skup = {}  # добије се празан рјечник, не БАШ скуп! --> зато `skup = set()` √
print(f"{str(skup):18s} | {type(skup)}")  # {} ...... | <class 'dict'>
print(f"{str(skup):18s} | duzina = {len(skup)}")
'''
>>> skup = {}
>>> skup
{}
>>> type(skup)
<class 'dict'>
>>> skup = dict()
>>> type(skup)
<class 'dict'>
>>> skup = set()
>>> type(skup)
<class 'set'>
'''

skup = set()
print(f"{str(skup):18s} | {type(skup)}")  # set() ... | <class 'set'>
'''
>>> skup = set({1, 2, 3, 3})
>>> skup
{1, 2, 3}
>>> skup = {1, 2, 3, 3}
>>> skup
{1, 2, 3}
>>> skup = {}
>>> skup
{}
>>> skup = set()
>>> skup
set()
>>> skup = set({})
>>> skup
set()
'''

skup = {"abb", "abcd", 2}
print(skup, "|", "duzina =", len(skup))  # {'abb', 'abcd', 2} | duzina = 3

skup = set(("b", "23a", 2.4))
print(f"{str(skup):18s} | t_i_p = {type(skup)}")
print(f"{str(skup):18s} | duzina = {len(skup)}")

skup = set({"b", "23a", 2.4})
print(f"{str(skup):18s} | t_i_p = {type(skup)}")
print(f"{str(skup):18s} | duzina = {len(skup)}")
'''
>>> skup = set({"b", "23a", 2.4})
>>> print(skup, type(skup))
{'23a', 2.4, 'b'} <class 'set'>

>>> skup = set(("b", "23a", 2.4))
>>> print(skup, type(skup))
{'23a', 2.4, 'b'} <class 'set'>
'''

# Nisu dozvoljeni duplikati! <-- LOOK! :eyes:

# add(val)
# val in set
# remove(val)
# set1.union(set2)          ili   operator `|`   <-- УНИЈА
# set1.intersection(set2)   ili   operator `&`   <-- ПРЕСЈЕК
# set1.difference(set2)     ili   operator `-`   <-- РАЗЛИКА СКУПОВА `A\B`

# Operator `^` - simetrična razlika, odnosno KOMPLEMENT PRESJEKA

# Operatori `>` ili `<` određuju da li je jedan skup NADSKUP ili PODSKUP drugog skupa,
# respektivno. √
# clear() ...

# funkcija koja uzima iterabilan objekat i konvertuje ga u `immutable` tip podatka √
frozenset()
