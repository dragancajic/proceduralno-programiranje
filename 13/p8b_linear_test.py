#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 23:40:20 2024

@author: dragancajic
"""

# Testiranje brzine svakog od algoritama za listu sa 10 000 000 elemenata.

import time

def linear_search_1(lst, value):
    i = 0
    while i != len(lst) and lst[i] != value:
        i = i + 1
    if i == len(lst):
        return -1
    else:
        return i

def linear_search_2(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

def linear_search_3(lst, value):
    i = 0
    while lst[i] != value:
        i = i + 1
    lst.pop()
    if i == len(lst):
        return -1
    else:
        return i


def time_it(search, L, v):
    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

def print_times(v, L):
    t1 = time.perf_counter()
    L.index(v)  # pronalazi indeks vijednosti v u listi L
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0
    # Računanje vremena za navedena tri algoritma
    while_time = time_it(linear_search_1, L, v)
    for_time = time_it(linear_search_2, L, v)
    sentinel_time = time_it(linear_search_3, L, v)
    print(f"{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}"
          .format(v, while_time, for_time, sentinel_time, index_time))

L = list(range(10000001))
print_times(10, L)
print_times(5000000, L)
print_times(1000000, L)

# Prokomentarisati rezultate.
# U sortiranoj listi od 1 milion elemenata linearni algoritmi NISU POGODNI
# za pretraživanje! √ LOOK! :eyes:
