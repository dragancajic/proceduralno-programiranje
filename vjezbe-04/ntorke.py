#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 13:07:46 2024

@author: dragancajic
"""

# ~ N-torke ~

# N-Tuple (N-torka) je tip podatka koji nam omogućava da u njega pohranjujemo
# skupove vrijednosti.
# U načelu n-torka se ponaša na način kao i lista, ali s jednom bitnom razlikom.
# RAZLIKA je ta da je n-torka nepromjenjiv (engl. immutable) tip podatka za
# razliku od liste koja je promjenjiva! √
# Takođe, liste koriste uglate zagrade `[]`, dok se kod pridruživanja
# vrijednosti u n-torku koriste oble zagrade `()`.
# Unutar n-torke, vrijednosti se odvajaju zarezom.

# Sintaksa za definisanje n-torke je:
# imeNtorke = (element1, element2, element3, ...)

# Ako se želi definisati prazna n-torka, to se radi na način:
imeNterca = ()  # или овако: `prazna_ntorka = tuple()` √

# imeNtorke[indeks]
# imeNtorke[pocetniIndeks:zavrsniIndeks]

# ОПРЕЗ! конструктор tuple(), па тек онда скуп вриједности ("abc", "bb") √
ntorka = tuple(("abc", "bb"))
# или
ntorka = ("abc", "bb")  # √
print(ntorka)
'''
>>> ntorka = ("abc", "bb")
>>> ntorka
('abc', 'bb')
>>> ntorka = tuple(("abc", "bb"))
>>> ntorka
('abc', 'bb')
'''

# (v1, v2, ..., *v) = ntorka
'''
>>> ntorka = ('abc', 'bb', 'cc', 'dd')
>>> ntorka
('abc', 'bb', 'cc', 'dd')
>>> (value1, value2, value3, value4) = ntorka
>>> print(value1)
abc
>>> value1
'abc'
>>> len(ntorka)
4
>>> print(len(ntorka))
4
'''
print(ntorka)
print(ntorka.count("bb"))  # 1
print(ntorka.count("dd"))  # 0

(value1, value2) = ntorka
print(value1, value2)  # abc bb
del ntorka
