#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:08:33 2023
Modified @ Thu 09 May 2024 18:56:32

@author: dragancajic
"""

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
SUM_LIST = 0

'''
~ for loop syntax ~

for val in sequence:
    loop body
'''
# iterate over the list
for val in numbers:
    # sum_list = sum_list + val
    SUM_LIST += val

print("The sum is:", SUM_LIST)  # The sum is: 48

# v a r i a t i o n s
# ~-----------------~
# for val in range(n)
# for val in range(1, n, 2)
# for val in list(range(10))

N = 10
for val in range(N):
    print(val, end=' ')  # 0 1 2 3 4 5 6 7 8 9

print()  # empty line

for val in range(1, N, 2):
    print(val, end=' ')  # 1 3 5 7 9

print()  # empty line

for val in list(range(N)):
    print(val, end=' ')  # 0 1 2 3 4 5 6 7 8 9
