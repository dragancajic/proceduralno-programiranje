#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 00:33:23 2023

@author: dragancajic
"""
# nije potrebno importovati za ugradjenu abs() funkciju!
import math;  # za math.fabs() ----> UVIJEK vraca float!

#EPSILON = 0.000001
EPSILON = 0.00001
#EPSILON = 0.5
#EPSILON = 0.1

s = int(input("Unesite prirodni broj za koji trazimo kvadratni korijen: "))
x0 = float(input("Dajte procjenu vrijednosti kvadratnog korijena broja: "))

xn = x0
brojac = 0
while (True):
    temp_xi = xn
    print("pocetna vrijednost xn =", xn)
    xn = (xn + (s / xn)) / 2
    print("trenutna vrijednost xn =", xn)
    print("trenutno |xn - temp_xi| =", math.fabs(xn - temp_xi))
    brojac = brojac + 1
    print("kraj ciklusa broj: ", brojac)
    print("~-~-~-~-~-~-~-~-~-~-~-~-~-~")
    
    if math.fabs(xn - temp_xi) <= EPSILON:
        break

print("Vrijednost kvadratnog korijena broja {0} je: {1:.5f}".format(s, xn))
