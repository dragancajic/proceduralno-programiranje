#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 01:49:03 2023

@author: dragancajic
"""


def summing(*arg):
    """Funkcija s proizvoljnim brojem argumenata"""
    lista = list(*arg)
    suma = 0

    for broj in lista:
        suma = broj + suma

    return suma


# suma elemenata liste
li1 = [4, 5, 3, 24, 6, 67, 1]
li2 = [4, 5, 3, 24, 6, 67, 1, -10]
li3 = [4, 5, 3, 24, 6, 67, 1, -10, 50]
print(summing(li1))  # zbir elemenata liste: 110
print(summing(li2))  # zbir elemenata liste: 100
print(summing(li3))  # zbir elemenata liste: 150
