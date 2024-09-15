#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:11:18 2024

@author: dragancajic
"""

# Zadatak 4

"""
Na programskom jeziku Python napisati program koji pronalazi i ispisuje sve
nekorektne e-mail adrese iz zadatate datoteke. Smatrati da korektna adresa
ima oblik local@domain pri čemu važi sljedeće:
 - Oba dijela adrese (local i domain) smiju da sadrže slova, brojeve, tačke,
   crtice i pluseve;
 - Oba dijela adrese moraju da počinju slovom;
 - Prvi dio (local) ne smije da ima više od 64 karaktera;
 - Drugi dio (domain) mora da se završi tačkom praćenom sa dva ili tri slova.
"""
'''
Primjer datoteke:

fica@student.etf.rs
dora.gmail.com
5a5a@yahoo.com
pavlovic.tea@student.etf.bg.ac.rs
i++@yahoo.com
jela_petrovic@gmail.com
a"b(c)d,e:f;g<h>i[j\k]l@etf.rs
d@j.edu
f121p-h0m3@dva+2.mkv
aleksandar@mail.mp3
a123456785678901234567890123436++@etf.bg.ac.rs
'''

import re

pattern = re.compile(r"^[a-zA-Z][\w.+-]{0,63}@[a-zA-Z][\w.+-]*.[a-zA-Z]{2,3}$")

with open("mejlovi.txt") as mails:
    for mail in mails:
        if not pattern.match(mail):
            print(mail.strip())
