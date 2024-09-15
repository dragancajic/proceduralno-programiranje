#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 02:00:38 2023

@author: dragancajic

~ Reduce

Zadatak: Sabrati sve brojeve u listi pomocu reduce.
"""
import functools

def saberi(x, y):
    return x + y

lista = [1, 2, 10, 4, 3, 19]

zbir = functools.reduce(saberi, lista)

print("Zbir je:", zbir)
