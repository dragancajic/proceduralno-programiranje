#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:41:01 2023

@author: dragancajic

~ Map
"""

def addition(n):
    return n + n


# lista sastavljena od dupliranih elemenata
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
