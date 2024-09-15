#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:01:52 2024

@author: dragancajic
"""

# • Predstavljanje ponavljanja •

# » Kreiranje ponavljanja karaktera:
# Za kreiranje se koriste specijalni karakteri `{ }` unutar kojih se navodi
# BROJ PONAVLJANJA.

# --------|------|
# Primjer - Opis |
# --------|------|
# {m}     - Prethodno navedeni karakter se ponavlja tačno m puta.
# {m,n}   - Prethodno navedeni karakter se ponavlja najmanje m, a najviše n puta.
# {m,}    - Prethodno navedeni karakter se ponavlja najmanje m puta, ne postoji
#           gornja granica.
# {,n}    - Prethodno navedeni karakter se ponavlja najviše n puta, ne postoji
#           donja granica.


# » Korišćenje postojećih ponavljanja:
# Koriste se specijalni karakteri `?`,`*` i `+`.

# --------------------|-----------------|------|
# Specijalni karakter - Ekvivalentno sa - Opis |
# --------------------|-----------------|------|
#  ?  - {0,1}  - Prethodno navedeni karakter se pojavljuje jednom ili nijednom.
#  *  - {0,}   - Prethodno navedeni karakter se ponavlja proizvoljan broj puta;
#                ne postoje ni gornja ni donja granica.
#  +  - {1,}   - Prethodno navedeni karakter se ponavlja najmanje jedanput, a
#                ne postoji gornja granica.
