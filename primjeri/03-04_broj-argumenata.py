#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 01:49:03 2023

@author: dragancajic
"""

def summing(*arg):
    """Funkcija s proizvoljnim brojem argumenata"""
    li = list(*arg)
    sum = 0
    
    for val in li:
        sum = val + sum
        
    return sum


# suma elemenata liste
li = [4, 5, 3, 24, 6, 67, 1]
print(summing(li))
