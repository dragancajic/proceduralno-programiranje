#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:08:33 2023

@author: dragancajic
"""

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

'''
~ for loop syntax ~

for val in sequence:
    loop body
'''
# iterate over the list
for val in numbers:
    # sum = sum + val
    sum += val

print("The sum is:", sum)
'''
v a r i a t i o n s

for val in range(n)
for val in range(1, n, 2)
for val in list(range(10))
'''
