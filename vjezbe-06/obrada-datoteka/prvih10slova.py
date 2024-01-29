#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:09:58 2024

@author: dragancajic
"""

# Ispis prvih 10 slova iz datoteke | `read([chars: int])`
"""
Definition : read()

Read at most n characters from stream.

Read from underlying buffer until we have n characters or we hit EOF.
If n is negative or omitted, read until EOF. √
"""
import os

print(os.getcwd())
# /home/dragancajic/Devs/pmfbl/pp/vjezbe-06/obrada-datoteka

#os.chdir('./pmfbl/pp/vjezbe-06/')
#os.getcwd()

with open('./linije-teksta.txt', 'r') as example_file:
    first_ten_chars = example_file.read(10)  # read(num_of_chars)
    the_rest = example_file.read()
    
print("Prvih 10 slova:", first_ten_chars)
print("Ostatak:", the_rest)
