#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:41:53 2023

@author: dragancajic
"""

ntorka1 = ("proceduralno", "programiranje", "razbija!")

for elem in ntorka1:
    print(elem)

ntorka2 = ("koristeci", "python", "jezik!")

ntorka = ntorka1[:-1] + tuple(ntorka2[::2]) + tuple(ntorka2[1:-1])

print("-" * 15)

for elem in ntorka:
    print(elem, end=' ')

print('\n' + str(len(ntorka)))  # '\n' + '5'
print(ntorka.count('jezik'))    # 0
print(ntorka.count('jezik!'))   # 1
