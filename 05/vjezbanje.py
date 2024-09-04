#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:43:42 2024

@author: dragancajic
"""

# ~ Skupovi ~

# Vježba 1:
# Napravite 2 skupa podataka i napunite ih proizvoljnim vrijednostima, te nakon toga
# napravite uniju i presjek tih skupova te ispišite rezultat i za uniju i za presjek.

predmeti1 = {
    'Proceduralno programiranje',
    'Osnove programiranja 2',
    'Uvod u veb tehnologije'
}
predmeti2 = {'IT i društvo', 'Osnove programiranja 2', 'Engleski jezik 1'}

print(predmeti1 | predmeti2)  # unija skupova
print(predmeti1 & predmeti2)  # presjek skupova


# ~ Rječnici ~

# Vježba 2:
# 1. Napravite rječnik `osoba` s ključevima `ime`, `prezime`, `godine`.
# Vrijednosti pridružene ključevima odredite sami. Ispišite samo vrijednosti
# u rječniku koristeći `for` petlju.

# 2. U rječnik kreiran u prethodnom zadatku dodajte novi par {kljuc : vrijednost}.
# Ključ može biti `adresa`, `JMB` ili nešto slično.

# 3. Iz rječnika korištenog u prethodnom zadatku izbrišite element `godine`,
# te ispišite rječnik.

osoba = {'ime': "Aleksandar", 'prezime': "Kukolj", 'godine': 32}
print('-' * 10)
for value in osoba.values():
    print(value)
print('-' * 10)
# ~ output:
# ----------
# Aleksandar
# Kukolj
# 32
# ----------

osoba.update({'zanimanje': "професионални џудиста"})
print('-' * 54)
for kljuc, vrijednost in osoba.items():
    print(f"kljuc = {kljuc}, vrijednost = {vrijednost}")
print('-' * 54)
# ~ output:
# ------------------------------------------------------
# kljuc = ime, vrijednost = Aleksandar
# kljuc = prezime, vrijednost = Kukolj
# kljuc = godine, vrijednost = 32
# kljuc = zanimanje, vrijednost = професионални џудиста
# ------------------------------------------------------

del osoba['godine']
print('-' * 37)
for kljuc, vrijednost in osoba.items():
    print(f"| {kljuc:9s} | {vrijednost:21s} |")
print('-' * 37)


# ~ Learning Material ~

# 1 ~ Python's F-String for String Interpolation and Formatting - Real Python
# https://realpython.com/python-f-strings/

# 2 ~ Strings and Character Data in Python - Real Python :eyes:
# https://realpython.com/python-strings/

# 3 ~ Python String Formatting Best Practices - Real Python
# https://realpython.com/python-string-formatting/

# 4 | When to Use a List Comprehension in Python - Real Python :eyes:
# https://realpython.com/list-comprehension-python/


# ~ N-torke ~

# Vježba 3:
# 1. Napravite n-terac u kojem su pohranjeni samoglasnici.
#    Ispišite prva tri samoglasnika.
# 2. Isprobajte promijeniti ili izbrisati element n-terca.

samoglasnici = ('a', 'e', 'i', 'o', 'u')
print(samoglasnici[0])     # a
print(samoglasnici[4])     # u
print(samoglasnici[0:3])   # ('a', 'e', 'i') <-> 0, 1, 2
print(type(samoglasnici))  # <class 'tuple'>

#samoglasnici[0] = 'A'
# TypeError: 'tuple' object does not support item assignment
print(samoglasnici[0].capitalize())  # A
print(samoglasnici)  # ('a', 'e', 'i', 'o', 'u')
