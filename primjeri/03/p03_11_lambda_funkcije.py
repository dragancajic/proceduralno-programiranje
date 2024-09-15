#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:14:36 2023

@author: dragancajic
"""

lambda_cube = lambda y: y * y * y
print(lambda_cube(2))
print(type(lambda_cube))

tabela = [lambda x = x: x * 10 for x in range(1, 5)]

# for broj in tabela:
#     print(broj)

# ~ Output:
# <function <listcomp>.<lambda> at 0x72a73c1a1af0>
# <function <listcomp>.<lambda> at 0x72a73c1a1b80>
# <function <listcomp>.<lambda> at 0x72a73c1a1c10>
# <function <listcomp>.<lambda> at 0x72a73c1a1ca0>

maximum = lambda a, b: a if (a > b) else b
print(maximum(3, -6))

# lista sastavljena od najvecih elemenata listi liste List
# koristiti lambda funkciju (ugnijezdene)
List = [[2, 3, 4], [1, 4, 16, 64], [3, 6, 9, 12]]

lista_max = []
for podlist in List:
    max_elem = podlist[0]
    for elem in podlist:
        if elem > max_elem:
            max_elem = elem
    print(max_elem)
    lista_max.append(max_elem)

print(lista_max)
