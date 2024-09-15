#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:25:18 2024

@author: dragancajic
"""

# Zadatak 9

# Za listu brojeva izračunati zbir cifara svih brojeva.

#from functools import reduce  # TODO: пробај "упослити" `reduce`! ;-)

brojevi = [10, 15, 13, 20, 11, 13]

def cifre(n):
    cifre_broja = []
    if n == 0:
        return [0]
    while n > 0:
        c = n % 10
        n //= 10
        cifre_broja.insert(0, c)
    return cifre_broja

lista_cifara = list([cifre(broj) for broj in brojevi])
print(lista_cifara)  # [[1, 0], [1, 5], [1, 3], [2, 0], [1, 1], [1, 3]]
suma = sum([sum(cifre) for cifre in lista_cifara])  # (1 + 6 + 4 + 2 + 2 + 4)
print(suma)  # 19
