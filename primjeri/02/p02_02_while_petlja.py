#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:21:52 2023
Modified @ Thu 09 May 2024 19:00:10

@author: dragancajic
"""

# sum = 1 + 2 + 3 + ... + n
# 1 + 2 + 3 + ... + n = n * (n + 1) / 2

n = int(input("Enter n: "))
# n = 5   # sum = 15
# n = 10  # sum = 55

# while iterative loop
'''
~ while loop syntax ~

while test_expression:
    loop body
'''

# initialize sum and counter
SUM_NUMS = 0
i = 1
while i <= n:
    SUM_NUMS = SUM_NUMS + i
    #print(f"temp sum: {SUM_NUMS:4d}, temp counter: {i:4d}")
    i = i + 1  # update counter

# print the sum
print("The sum is:", SUM_NUMS)
