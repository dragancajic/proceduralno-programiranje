#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:24:39 2024

@author: dragancajic

~ Домаћи задатак 3 ~
"""

broj = int(input('Unesite cetvorocifren broj: '))

jedinice = broj % 10
desetice = (broj // 10) % 10
stotice = (broj // 100) % 10
hiljade = broj // 1000

proizvod_cifara = jedinice * desetice * stotice * hiljade

suma_kvadrata = jedinice * jedinice + desetice * desetice + stotice *  stotice \
    + hiljade * hiljade

obrnut_broj = jedinice * 1000 + desetice * 100 + stotice * 10 + hiljade

novi_broj = hiljade * 1000 + jedinice * 100 + desetice * 10 + stotice

print('Proizvod cifara:', proizvod_cifara)
print('Suma kvadrata cifara:', suma_kvadrata)
print('Broj u obrnutom poretku:', obrnut_broj)
print('Broj sa zamenjenom cifrom jedinica i stotina:', novi_broj)
