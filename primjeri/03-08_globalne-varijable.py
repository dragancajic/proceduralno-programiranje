#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:21:37 2023

@author: dragancajic

~ Globalne varijable

> Rijec 'global' daje `WRITE` pristup varijabli (koja se nalazi van funkcije)
unutar funkcije !!! <-- LOOK!
"""

c = 0  # global variable

def add():
    global c
    c = c + 2  # increment by 2
    print("Inside add():", c)  # Inside add(): 2


add()
print("In main:", c)  # In main: 2
