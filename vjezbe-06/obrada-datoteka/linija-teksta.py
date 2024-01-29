#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 17:33:57 2024

@author: dragancajic
"""

# Korištenje `readline` tehnike za preskakanje ispisivanja reda iz datoteke.
# Sabiranje vrijednosti iz datoteke.
"""
Definition : readline(size=-1, /)

Read and return a line from the stream.

If size is specified, at most size bytes will be read.

The line terminator is always b'n' for binary files;
for text files, the newlines argument to open can be
used to select the line terminator(s) recognized.
"""

with open('podaci.txt', 'r') as podaci_file:
# Čitanje i preskakanje naslova
    line = podaci_file.readline()  # прочитај прву линију (наслов) из 'podaci.txt'
    print(line.strip())  # уклони карактер за нови ред, тј. '\n' из линије наслова
# Nastavak čitanja i preskakanja komentara dok se ne dođe do prvog podatka
    data = podaci_file.readline().strip()  # уклони "бјелине", нпр. '\n'
    print(data)  #Neki komentar koji je takođe potrebno preskočiti
    while data.startswith('#'):
        data = podaci_file.readline().strip()
        #print(data)  # ипак је прочитан '22', након треће линије текста! ;-)
    print(data, type(data))    # 22 <class 'str'>
# Prethodno smo došli do prvog "brojčanog" stringa -> kastujmo ga u broj
    total = int(data)  # бројчани податак ---> 22
    print(total, type(total))  # 22 <class 'int'>
# Čitanje ostalih podataka/brojeva i dodavanje u zbir
    for data in podaci_file:
        total = total + int(data.strip())
        print(total)
print("Zbir podataka:", total)
