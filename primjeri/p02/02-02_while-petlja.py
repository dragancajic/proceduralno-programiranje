#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:21:52 2023
Modified @ Sun 04 Feb 2024 14:14:47

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
sum_nums = 0
i = 1
while i <= n:
    sum_nums = sum_nums + i
    print(f"temp sum: {sum_nums:4d}, temp counter: {i:4d}")
    i = i + 1  # update counter

# print the sum
print("The sum is:", sum_nums)
