#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:07:15 2024

@author: dragancajic

~ Домаћи задатак 1 ~
"""

# Ucitavanje vremena poletanja. [format unosa: 'sat minut'], npr. '8 5'
poletanje_sat, poletanje_minut = input('Unesite vreme poletanja: ').split(' ')

# Ucitavanje vremena sletanja. [format unosa: 'sat minut'], npr. '12 41'
sletanje_sat, sletanje_minut = input('Unesite vreme sletanja: ').split()

# Pretvaranje oba vremena (u `int`, pa) u minute radi lakseg racunanja razlike.
poletanje = int(poletanje_sat) * 60 + int(poletanje_minut)
sletanje = int(sletanje_sat) * 60 + int(sletanje_minut)

# Racunanje razlike u minutima izmedju sletanja i poletanja.
duzina = sletanje - poletanje

# Pretvaranje razlike u minutama u razliku u satima i minutima.
# Razlika u satima se dobija celobrojnim deljenjem broja minuta
# sa 60.
# Preostali broj minuta se dobija kao ostatak pri deljenju sa 60.
duzina_sat = duzina // 60

duzina_minut = duzina % 60
# ili na II nacin:
# duzina_minut = duzina - duzina_sat * 60  # √ RADI! ;-) Драган Ћајић

# Ispis rezultata.
print(f'Duzina trajanja leta: {duzina_sat} h i {duzina_minut} min')
