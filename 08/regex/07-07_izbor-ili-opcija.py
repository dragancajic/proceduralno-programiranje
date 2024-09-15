#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:59:14 2024

@author: dragancajic
"""

# ■ Izbor ■ `ILI` опција "pipe character" `|`

# Za izbor se koristi specijalni karakter `|`.

# Primjer 1

import re

sablon = re.compile(r"a|b")

print(sablon.match("a"))  # <re.Match object; span=(0, 1), match='a'>
print(sablon.match("b"))  # <re.Match object; span=(0, 1), match='b'>
print(sablon.match("c"))  # None

print('-' * 42)


# Primjer 2

sablon = re.compile(r"a|b|c")

print(sablon.match("a"))  # <re.Match object; span=(0, 1), match='a'>
print(sablon.match("b"))  # <re.Match object; span=(0, 1), match='b'>
print(sablon.match("c"))  # <re.Match object; span=(0, 1), match='c'>

print('~' * 42)


# Primjer 3

sablon = re.compile(r"(a|b)c")

print(sablon.match("ac"))   # <re.Match object; span=(0, 2), match='ac'>
print(sablon.match("bc"))   # <re.Match object; span=(0, 2), match='bc'>
print(sablon.match("abc"))  # None
print(sablon.match("ab"))   # None
print(sablon.match("c"))    # None
