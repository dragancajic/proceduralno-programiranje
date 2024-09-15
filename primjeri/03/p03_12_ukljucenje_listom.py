#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 21:11:31 2024

@author: dragancajic

~ ОБУХВАТАЊЕ ЛИСТОМ / УКЉУЧЕЊЕ У ЛИСТУ / **List Comprehension**
"""

lista1 = [x+y for x in [5, 10, 15] for y in [20, 25, 30]]
print(lista1)  # [25, 30, 35, 30, 35, 40, 35, 40, 45] <-- Декартов производ

lista2 = [
    x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')]
print(lista2)  # ['sP', 'sA', 'mP', 'mA']

lista3 = [(x, y) for x in range(5) if x %
          2 == 0 for y in range(5) if y % 2 == 0]
print(lista3)
# [(0, 0), (0, 2), (0, 4), (2, 0), (2, 2), (2, 4), (4, 0), (4, 2), (4, 4)]
# Декартов производ парних бројева из обје дате листе: `x` и `y`
