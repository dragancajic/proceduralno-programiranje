#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:44:39 2023

@author: dragancajic

~ Kljuc-vrijednost prenos argumenata
prosljedjivanje liste argumenata promjenljive duzine s kljucnim rijecima
"""

# **kwargs for var number of kwords args
def my_fun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

# driver code
my_fun(first = 'Geeks', last = 'for')


def myFun(**kwargs):
    # tijelo funkcije
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

# poziv
#myFun({"arg1": "var1", "arg2": "var2", "arg3": "var3"})  # ne prolazi!
myFun(arg1 = "var1", arg2 = "var2", arg3 = "var3")  # P R O L A Z I!
