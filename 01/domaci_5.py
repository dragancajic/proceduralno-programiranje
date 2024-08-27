#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:39:38 2024

@author: dragancajic

~ Домаћи задатак 5 ~
"""

m = int(input('Unesite pozitivan ceo broj: '))  # 12345, 50_000_000
k = int(input('Unesite pozitivan dvocifren broj: '))  # 67; 12

levo = m // 1000
desno = m % 1000
# print('levo:', levo, 'desno:', desno)

novi_broj = levo * 100000 + k * 1000 + desno

print('Rezultat:', novi_broj) # 12345, 67 -> 1267345; 5000012000
