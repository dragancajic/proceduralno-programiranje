#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:50:18 2023

@author: dragancajic
"""

def myfunc(arg1, arg2, arg3, arg4):
    print(arg1, arg2, arg3, arg4)

def printer(message):
    print('Hello ' + message)

def adder(a, b = 1, *c):
    return a + b + c[0]


# TODO: provjeri detaljnije argumente funkcija / prenos
# pozivi funkcija
rest = ['spam', 'eggs', 'milk', 'coffee', 'tea']
ham = 'nice ham'
#myfunc('spam', 'eggs', meat = ham, *rest)
printer("Python!")
#adder((3, 4, 5, 6))
