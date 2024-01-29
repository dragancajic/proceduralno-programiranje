#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:35:53 2024

@author: dragancajic
"""

# Pisanje primjera uz pomoć `StringIO`

from io import StringIO

input_string = '1.3 3.4\n2 4.2\n-1 1\n'
infile = StringIO(input_string)

# испис (само) једне линије из улазне ниске карактера / стринга
prva_linija = infile.readline()
#print(prva_linija)          # 1.3 3.4\n
print(prva_linija.strip())   # 1.3 3.4

# читање и испис друге линије из улазне ниске карактера / стринга
druga_linija = infile.readline()
#print(druga_linija)          # 2 4.2\n
print(druga_linija.strip())   # 2 4.2

# читање и испис треће линије из улазне ниске карактера / стринга
treca_linija = infile.readline()
#print(treca_linija)          # -1 1\n
print(treca_linija.strip())   # -1 1

print("~-" * 5)

"""
write

Definition : write(which is always equal to the length of the string, /)

Write string to stream. Returns the number of characters written
(which is always equal to the length of the string).
"""
outfile = StringIO()
#niska = outfile.write('123456789\n')
#print(niska)  # 9 <-- дужина ниске √

#duzina_niske = outfile.write('2 4.2 6.2\n')
#print(duzina_niske)  # 9 карактера + '\n' -> 10 (дужина стринга) √

print("-~" * 5)

print(outfile.write('1.3 3.4 4.7\n'))  # 11 карактера + '\n' -> 12 √
print(outfile.write('2 4.2 6.2\n'))    #  9 карактера + '\n' -> 10 √
print(outfile.write('-1 1 0.0\n'))     #  8 карактера + '\n' -> 9  √

print("~*" * 6)

"""
getvalue

Definition : getvalue()

Retrieve the entire contents of the object.
"""
print(outfile.getvalue())
