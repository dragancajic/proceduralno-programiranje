#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:33:57 2024

@author: dragancajic
"""

# ~ Funkcije i metode ~

# Za kreiranje izraza koristi se funkcija compile()

import re

sablon_rijec = re.compile(r"rijec")
sablon_od = re.compile(r"od")
tekst = "rijeci od cetiri slova"


# Za pretragu stringa koriste se metode `match()`, `search()`, `finditer()`.

# Match objekti | metoda `match()`
"""
Match objekti sadrže informacije o rezultatima pretrage.
Ukoliko nema pogotka, umesto Match objekta povratna vrijednost je `None`.
"""
print(sablon_rijec.match(tekst))  # <re.Match object; span=(0, 5), match='rijec'>
print(sablon_od.match(tekst))     # None


# Metoda `search()`

# Pretražuje string da bi ispitala da li sadrži patern/шаблон
# (traži PRVO POJAVLJIVANJE paterna/шаблона u stringu)!

print(sablon_rijec.search(tekst))  # <re.Match object; span=(0, 5), match='rijec'>
print(sablon_od.search(tekst))     # <re.Match object; span=(7, 9), match='od'>


# Metoda `finditer()`

# Proširen je `tekst` za pretragu, radi lakšeg razumijevanja metoda
# `finditer()`, koji vraća SVA POJAVLJIVANJA određene riječi u stringu.

sablon_rijec = re.compile(r"rijec")
sablon_od = re.compile(r"od")
tekst = "rijeci od cetiri slova i rijeci od tri slova"

for pogodak in sablon_rijec.finditer(tekst):
    print(pogodak)
'''
<re.Match object; span=(0, 5), match='rijec'>
<re.Match object; span=(25, 30), match='rijec'>
'''


# ~ Metode `start()`, `end()` i `span()` ~

# Metode `start()`, `end()` i `span()` vraćaju
# informacije o poziciji pogotka unutar stringa.

sablon = re.compile(r"ovu")
tekst = "pronadji ovu rijec"
pogodak = sablon.search(tekst)  # <re.Match object; span=(9, 12), match='ovu'>

if pogodak:
    pocetak = pogodak.start()   # 9
    kraj = pogodak.end()        # 12
    print(tekst[pocetak:kraj])  # ovu
    print(pogodak.span())       # (9, 12)
