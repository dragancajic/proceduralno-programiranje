#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 00:19:55 2023

@author: dragancajic

~ Неограничен број параметара: примјер
"""

def arithmetic_mean(first, *values):
    """This function calculates the arithmetic mean of non-empty
       arbitrary number of numerical values"""
    
    return (first + sum(values)) / (1 + len(values))


print(arithmetic_mean(45, 32, 89, 78))                    # 61.0
print(arithmetic_mean(8989.8, 78787.78, 3453, 78778.73))  # 42502.3275
print(arithmetic_mean(45, 32))                            # 38.5
print(arithmetic_mean(45))                                # 45.0
