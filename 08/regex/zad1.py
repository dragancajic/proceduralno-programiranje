# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 10:59:46 2022

@author: User
"""

import re, sys, getopt

ifile = ''
ofile = ''
z = 0

try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:o:z:')
    
    for opt, arg in opts:
        if opt == '-i':
            ifile = arg
        elif opt == '-o':
            ofile = arg
        elif opt == '-z':
            if arg.isdigit():
                z = int(arg)
                
                if z > 3 or z < 1:
                    print('pogresan unos')
                    exit(1)
            else:
                print('pogresan unos')
                exit(1)
except getopt.GetoptError as e:
    print('greska: ', e)
    
if ifile != '':
    with open(ifile) as f:
        contents = f.readlines()
        
print(contents)

#soba, dv : 220
pattern = re.compile(r'(\w+),\s(\w+\s?(\w+)?)\s*:\s*(\d+)')

if z == 1:
    l1 = []
    for content in contents:
        match = re.search(pattern, content)
        if match.group(4) is not None:
            if int(match.group(4)) > 120:
                l1.append(match.group(1) + ', ' + match.group(2))
                
    if ofile != '':
        with open(ofile, 'w') as f:
            f.write('Sve usluge cija je cijena veca od 120KM:\n')
            for i in l1:
                f.write(i + '\n')
elif z == 2:
    l2 = []
    for content in contents:
        match = re.search(pattern, content)
        if match.group(4) is not None:
            if int(match.group(4)) >= 50 and int(match.group(4)) < 150:
                l2.append(match.group(2))
                
    if ofile != '':
        with open(ofile, 'w') as f:
            f.write('Svi tipovi usluga sa cijenom izmedju 50KM i 90KM:\n')
            for i in l2:
                f.write(i + '\n')
elif z == 3:
    l3 = []
    p = []
    
    usluge = dict()
 
    for content in contents:
        match = re.search(pattern, content)
        if match.group(1) not in usluge.keys():
            usluge[match.group(1)] = list()

        usluge[match.group(1)].append(int(match.group(4)))
    
    for i in usluge.keys():
        prosjek = sum(usluge[i])/len(usluge[i])
        if prosjek < 90:
            l3.append(i)
        
    if ofile != '':
        with open(ofile, 'w') as f:
            f.write('Sve usluge hotela cija je prosjecna cijena tipa manja od 90KM:\n')
            for i in l3:  #l2 nije definisano treba da stoji l3 pa sam ispravila kod - Milica
                f.write(i + '\n')
