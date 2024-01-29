#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:46:20 2024

@author: dragancajic
"""

with open('planete.txt', 'r') as planets_file:
    planets = planets_file.readlines()

for planet in reversed(planets):
    print(planet.strip())

print(planets)
'''
[
 'Merkur\n',
 'Venera\n',
 'Zemlja\n',
 'Mars\n',
 'Jupiter\n',
 'Saturn\n',
 'Uran\n',
 'Neptun\n',
 'Pluton'
]
'''
