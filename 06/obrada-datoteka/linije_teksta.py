#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:35:27 2024

@author: dragancajic
"""

# Раздвој текст по "бјелинама" - читај линије текста | `readlines()`

# Definition : readlines(hint=-1, /)

# Return a list of lines from the stream.

# hint can be specified to control the number of lines read: no more lines will
# be read if the total size (in bytes/characters) of all lines so far exceeds hint.


with open('linije-teksta.txt', 'r', encoding='utf-8') as example_file:
    lines = example_file.readlines()
print(lines)

# output:

# ['Prva linija teksta\n',
#  'Druga linija teksta\n',
#  'Treca linija teksta\n',
#  'Cetvrta linija teksta\n'
# ]
