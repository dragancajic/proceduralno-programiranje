#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:35:02 2024

@author: dragancajic
"""

# Zadatak 3

# Na programskom jeziku Python sastaviti funkciju koja učitanoj datoteci
# mijenja format u kom su zapisani podaci o studentu.
"""
Npr.

162/2018, Dorotea Pavlović
28/2019, Filip Ristić
413/2019, Jelena Petrović

Mijenja se u:

18/162, Pavlović Dorotea
19/28, Ristić Filip
19/413, Petrović Jelena
"""

import re

def rewrite(filename):
    with open(filename, "r+", encoding="UTF-8") as file:
        text = file.read()
        
        # групиши посљедње цифре године!
        pattern = re.compile(r"(\d{1,4})/\d{2}(\d{2}),\s+(\w+)\s+(\w+)")
        
        # промијени позицију група: 1, 2, 3, 4 <--- A-HA! √
        new_text = pattern.sub(r"\2/\1, \4 \3", text)
        file.seek(0)
        #file.truncate()
        file.write(new_text)
filename = input("Unesite naziv datoteke: ")  # studenti.txt
rewrite(filename)  # TODO: пронађи грешку у коду! :wink:

# Na linku ispod možete pročitati više o `r+`, `w+` i `a+`.
# link: https://mkyong.com/python/python-difference-between-r-w-and-a-in-open/#what-is-means-in-open
