#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:39:08 2023

@author: dragancajic

~ Разлика између функција у Пајтону и другим језицима
> Варијабла `bag` са default-ном вриједношћу се само једном креира--у времену
  компајлирања !!!
> Default-на вриједност се НЕ КРЕИРА у позиву функције!
"""
'''
def spammer(bag = []):
    bag.append("spam")
    return bag
'''
def spammer(bag = None):  # SOLUTION: make default `bag` value immutable!
    bag = []  # `None` is immutable type, so function can set dynamically
    bag.append("spam")  # (in runtime) value of variable bag to an empty list!
    return bag

# function calling
#print(spammer())  # OUTPUT: ['spam']
#print(spammer())  # OUTPUT: ['spam', 'spam']

# attribute __defaults__
for i in range(5):
    print(spammer())

print("spammer.__defaults__", spammer.__defaults__)
