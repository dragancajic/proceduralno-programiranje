#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 13:03:48 2024

@author: dragancajic
"""

# Zadatak 7

# Primjenom funkcije `filter` i `reduce`, izdvojiti iz početne liste
# rečenica one rečenice čija je dužina najduže riječi veća od 7.

#from functools import reduce  # TODO: пробај "упослити" `reduce`! ;-)

def najduza_rijec(recenica):
    #print("zadata recenica:", recenica)
    lista_rijeci = recenica.split()  # подијели реченицу по "бјелинама" | sep
    #print("lista rijeci:", lista_rijeci)
    najveca_duzina = max(len(rijec) for rijec in lista_rijeci)
    #print("duzina najduze rijeci:", najveca_duzina)
    return najveca_duzina

recenice = ['Ponedjeljak je prvi dan u sedmici.', 'Ja sam Milica.', 'Danas je utorak']
recenice = filter(lambda recenica:
                  recenica
                      if najduza_rijec(recenica) > 7
                      else '',
                  recenice)
# за сваку реченицу из листе реченица, врати само оне реченице чија је најдужа
# ријеч ДУЖА од 7 карактера! √
#print(recenice)        # <filter object at 0x7fa9a4791810>
#print(type(recenice))  # <class 'filter'>

for recenica in recenice:
    print(recenica)
