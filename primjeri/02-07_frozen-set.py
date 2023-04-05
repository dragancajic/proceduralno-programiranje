#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 03:10:54 2023

@author: dragancajic
"""

# creating list
favourite_subject = ["OS", "DBMS", "Algo"]

# making it frozenset type
f_subject = frozenset(favourite_subject)

# below line will generate error
f_subject[1] = "Networking"

# TypeError: 'frozenset' object does not support item assignment
