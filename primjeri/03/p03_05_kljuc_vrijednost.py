#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:44:39 2023

@author: dragancajic

~ Кључ-вриједност пренос аргумеанта
просљеђивање листе аргумената промјенљиве дужине с кључним ријечима
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
# myFun({"arg1": "var1", "arg2": "var2", "arg3": "var3"})  # ne prolazi!
# TypeError: myFun() takes 0 positional arguments but 1 was given

myFun(arg1 = "var1", arg2 = "var2", arg3 = "var3")  #  P R O L A Z I!
