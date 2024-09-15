#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:36:34 2024

@author: dragancajic
"""

# Korisni kodovi

filename = 'datoteka.txt'

# kreiranje prazne datoteke
with open(filename, "w", encoding='utf-8') as f:
    pass

filename01 = 'datoteka01.txt'

# prvi (I) način: čitanje `linija po linija`
with open(filename01, 'r', encoding='utf-8') as f:
    linija = f.readline()  # (method) def readline(__size: int = -1) -> str
    while linija.strip() != "":
        # print(linija)
        print(linija)
        linija = f.readline()

print()  # направи празан ред

# drugi (II) način: čitanje cijelog sadržaja
with open(filename01, 'r', encoding='utf-8') as f:
    sadrzaj = f.read()  # (method) def read(__size: int | None) -> str
    print(sadrzaj)

print()  # направи празан ред

# treći (III) način: čitanje sadržaja svih linija
with open(filename01, 'r', encoding='utf-8') as f:
    linije = f.readlines()  # (method) def readlines(__hint: int = -1) -> list[str]
    print(linije)

print()

# ~ metoda `seek(int)` -> енгл. whence [formal]:
# `From what place or origin or source` == (synonym) wherefrom [archaic].

# "pokazivač" se nalazi na početku sadržaja fajla, jer još uvijek ništa iz datoteke
# nije pročitano; pomoću metode `seek()` se pokazivač pomjera na 5. poziciju :eyes:
with open(filename01, 'r', encoding='utf-8') as f:
    f.seek(5)  # (method) def seek(__cookie: int, __whence: int = 0) « LOOK! :eyes:
    sadrzaj = f.read()
    print(sadrzaj)
