#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:55:44 2024

@author: dragancajic
"""

# ■ Grupisanje i grupe ■

# Za grupisanje se koriste specijalni karakteri `( )`.

import re

tekst = "abababab"
sablon = re.compile(r"(ab)*")

print(sablon.match(tekst))  # <re.Match object; span=(0, 8), match='abababab'>


# Primjer 1

tekst = "abababab"
sablon = re.compile(r"(a)(b)")

pogodak = sablon.match(tekst)

print(pogodak.group())      # ab
print(pogodak.group(0))     # ab
print(pogodak.group(1))     # a
print(pogodak.group(2))     # b
print(pogodak.group(1, 2))  # ('a', 'b')
print(pogodak.groups())     # ('a', 'b')


# Primjer 2

tekst = "abababab"
sablon = re.compile(r"(a(b))")

pogodak = sablon.match(tekst)

print(pogodak.group(0))  # ab
print(pogodak.group(1))  # ab
print(pogodak.group(2))  # b
