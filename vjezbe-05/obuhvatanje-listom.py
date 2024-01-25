#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:38:21 2024

@author: dragancajic
"""

# List Comprehension - primjer

# Transponovati matricu koristeći `List Comprehension` √
# [обухватање листом/укључивање у листу]
matrica = [[1, 2], [3,4], [5,6], [7,8]]  # матрица 4x2
transponovana = [[red[i] for red in matrica] for i in range(2)]
print (transponovana)  # [[1, 3, 5, 7], [2, 4, 6, 8]]


# пробајмо написати кôд који је еквивалентан претходном, БЕЗ обухватања листом,
# односно, пробајмо "распаковати" претходни кôд у циљу лакшег разумијевања кода:
transponovana = []
kolona = []
for i in range(2):  # иди по индексима колона
    for red in matrica:
        kolona.append(red[i])
        #print(kolona)
    transponovana.append(kolona)
    kolona = []
print(transponovana)  # [[1, 3, 5, 7], [2, 4, 6, 8]] <-- матрица 2x4

# ЗАКЉУЧАК: Обухватање(м) листом (енгл. List Comprehension) смањили смо број
# линија кода са девет (9) на само три (3) линије кода. Потребано је навићи
# се на синтаксу укључивања у листу/обухватања листом: [tijelo for iteracija],
# што је у случају нашег проблема транспоновања матрице:
# `[[tijelo unutrasnja-petlja iteracija] spoljasnja-petlja iteracija]`.
