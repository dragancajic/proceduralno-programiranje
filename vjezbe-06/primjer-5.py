#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:03:47 2024

@author: dragancajic
"""

# Primjer 5

import random

print(random.randrange(1, 5))       # 1, 2, 3, 4 <-- [1, 5)  korak 1
print(random.randrange(2, 10, 3))   # 2, 5, 8    <-- [2, 10) korak 3
print(random.randrange(20, 50, 3))  # [20, 50) korak 3
# 20, 23, 26, 29, ..., 32, 35, ..., 38, 41, 44, ..., 47 √
