#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:39:08 2023

@author: dragancajic

~ Razlika izmedju funkcija u python-u i drugim jezicima
> varijabla bag sa default-nom vrijednoscu se samo jednom kreira--u vremenu
  kompajliranja !!!
> default-na vrijednost se NE KREIRA u pozivu funkcije!
"""
'''
def spammer(bag = []):
    bag.append("spam")
    return bag
'''
def spammer(bag = None):  # SOLUTION: make default bag value immutable!
    bag = []  # None is immutable type, so function can set dynamically (in
    bag.append("spam")  # runtime) value of variable bag to an empty list !
    return bag

# function calling
#print(spammer())  # OUTPUT: ['spam']
#print(spammer())  # OUTPUT: ['spam', 'spam']

# attribute __defaults__
for i in range(5):
    print(spammer())

print("spammer.__defaults__", spammer.__defaults__)
