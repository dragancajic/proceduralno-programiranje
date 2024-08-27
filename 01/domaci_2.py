#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:23:52 2024

@author: dragancajic

~ Домаћи задатак 2 ~
"""

broj = int(input('Unesite trocifren broj: '))

jedinice = broj % 10
desetice = (broj // 10) % 10
stotine = broj // 100

novi_broj = jedinice * 100 + desetice * 10 + stotine

print('Obrnuto:', novi_broj)
