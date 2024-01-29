#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:31:41 2024

@author: dragancajic
"""

# U ovom primjeru koristi se čitanje i pisanju u datoteku. √

# Ulazna datoteka sadrži linije koje su sačinjene od dva broja odvojena jednim razmakom.

# Izlazna datoteka bi trebalo da u svakoj liniji sadrži po tri broja:
# prva dva broja su ulazni podaci, a treći broj je njihov zbir.

from typing import TextIO
#from io import StringIO

def sum_number_pairs(input_file: TextIO, output_file: TextIO) -> None:
    for number_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) + float(operands[1])
        new_line = '{0} {1}\n'.format(number_pair, total)
        output_file.write(new_line)


if __name__ == '__main__':
    with open('brojevi.txt', 'r') as input_file, \
        open('brojevi_suma.txt', 'w') as output_file:
        sum_number_pairs(input_file, output_file)
