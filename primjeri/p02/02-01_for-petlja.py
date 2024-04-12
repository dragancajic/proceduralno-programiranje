#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:08:33 2023
Modified @ Sat 06 Apr 2024 16:16:55

@author: dragancajic
"""

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum_list = 0

'''
~ for loop syntax ~

for val in sequence:
    loop body
'''
# iterate over the list
for val in numbers:
    # sum_list = sum_list + val
    sum_list += val

print("The sum is:", sum_list)  # The sum is: 48

# v a r i a t i o n s
# ~-----------------~
# for val in range(n)
# for val in range(1, n, 2)
# for val in list(range(10))

n = 10
for val in range(n):
    print(val, end=' ')  # 0 1 2 3 4 5 6 7 8 9

print()  # empty line

for val in range(1, n, 2):
    print(val, end=' ')  # 1 3 5 7 9

print()  # empty line

for val in list(range(n)):
    print(val, end=' ')  # 0 1 2 3 4 5 6 7 8 9
