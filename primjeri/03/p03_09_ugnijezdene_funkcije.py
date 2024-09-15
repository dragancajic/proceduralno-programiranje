#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:58:30 2023

@author: dragancajic
"""

def f1():
    x = 20
    x = x + 1
    
    def f2():
        global x  # <-- make it globally available!
        # nonlocal x
        x = 25
        x = x + 1
        print("Hello from f2():", x)
    
    #f2()
    print("Hello from f1():", x)
    #return 1
    f2()


print(f1())  # None <-- no `return` statement for `f1()`
print(x)     # 26 <-- variable x is now global variable!
