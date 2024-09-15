#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:25:26 2023

@author: dragancajic

~ Животни вијек варијабли
"""

y = 7

def my_func():
    x = 10
    #y = y + 1
    print("Vrijednost unutar funkcije:", x)  # Vrijednost unutar funkcije: 10

x = 20  # varijabla x van funkcije: *r e a d*  pristup unutar funkcije! LOOK!
y = 5
my_func()
print("Vrijednost van funkcije:", x)  # Vrijednost van funkcije: 20


def f():
    # print(s)    # This means a free occurrence, contradiction to being local
    s = "Pearl"  # This makes s local in f
    print(s)


s = "Python"
f()  # UnboundLocalError: local variable 's' referenced before assignment (lines: 27, 21)
print(s)
