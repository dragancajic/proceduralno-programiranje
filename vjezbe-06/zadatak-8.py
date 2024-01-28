#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:48:46 2024

@author: dragancajic
"""

# Zadatak 8 - rad sa datotekama

# Na slučajan način se generiše datoteka koja sadrzi brojeve iz intervala [3, 99].
# Navedena datoteka sadrži jedan broj u jednom redu. Generisanje brojeva se prekida
# kada se generišu dva broja čija je suma cifara jednaka (ti brojevi ne moraju biti
# uzastopni!).

# Sačuvati navedenu datoteku, te je opet otvoriti i pročitati njen sadržaj.
# Za svaki par generisanih brojeva čuvati njihov proizvod i broj koji se dobije
# kao proizvod njihovih cifara, te se navedenom proizvodu zamijene prva i
# posljednja cifra.

# Navedeni rezultat čuvati u istoj datoteci. Generisane brojeve i rezulat
# razdvojiti linijom koja sadrzi 20 znakova '='. Npr. generisani brojevi su:
#   3, 76, 14, 93, 87, 49
# (3, 76) 3*76 = 228, 3*7*6 = 126 -> 621, 228 < 621. Odnosno (3, 76) -> (228, 621).

# Sadržaj datoteke treba da bude:
#
# 3
# 76
# 14
# 93
# 87
# 49
# ====================
# (3, 76) -> (228, 621)
# (3, 14) -> (42, 21)
# (3, 93) -> (279, 18)
# (3, 87) -> (261, 861)
# ...
# (87, 49) -> (4263, 6012)

import random

def cifre_broja(n):
    if n == 0:
        return [0]
    cifre = []
    while n > 0:
        c = n % 10
        n //= 10
        cifre.insert(0, c)
    return cifre

def suma_cifara(n):
    cifre = cifre_broja(n)
    return sum(cifre)

def prekid_generisanja(lista):
    '''
    Funkcija koja provjerava da li se prekida generisanje brojeva, odnosno,
    provjeravamo da li postoji broj čija je suma cifara jednaka sumi cifara
    posljednjeg elementa liste.
    '''
    if lista == []:
        return False

    uslov = False
    s1 = suma_cifara(lista[-1])
    for e in lista[:-1]:
        s2 = suma_cifara(e)
        if s1 == s2:
            uslov = True
            break
    return uslov

def generisi_datoteku(naziv_datoteke, od, do):
    '''
    Funkcija koja generiše sadržaj datoteke. Ova funkcija kreira navedenu datoteku
        `naziv_datoteke`: naziv datoteke koja se kreira
        `od`: donja granica brojeva koji se generišu
        `do`: gornja granica brojeva koji se generišu
    '''
    generisana_lista = []
    with open(naziv_datoteke, "w") as f:
        while True:
            novi_broj = random.randint(od, do)
            f.write(str(novi_broj))
            generisana_lista.append(novi_broj)
            if prekid_generisanja(generisana_lista):
                break
            # prebacujemo se u novi red, ali izbjegavamo da posljednja linija
            # bude prazna!
            f.write("\n")

def citaj_sadrzaj_datoteke(naziv_datoteke):
    with open(naziv_datoteke, 'r') as f:
        lista_brojeva = f.readlines()
    lista_brojeva = [int(br) for br in lista_brojeva]
    return lista_brojeva

def uredjeni_parovi(lista):
    parovi = []
    for i, k in enumerate(lista[:-1]):
        for k2 in lista[i+1:]:
            parovi.append((k, k2))
    return parovi

def broj_od_cifara(lista_cifara):
    '''Kreira novi broj koji se sastoji od cifara koje se dobijaju kao ulazni
        parametar
        `param lista_cifara`: cifre broja
    '''
    n = 0
    for c in lista_cifara:
        n *= 10
        n += c
    return n

def zamijeni_prvu_i_posljednju_cifru(n):
    cifre = cifre_broja(n)
    prva = cifre[0]
    posljednja = cifre[-1]
    # mijenjamo prvu i posljednju cifru u listi
    cifre[0] = posljednja
    cifre[-1] = prva

    # na jednostavniji način smo mogli zamijeniti prvu i posljednju cifru u
    # listi: `cifre[0], cifre[-1] = cifre[-1], cifre[0]`. √

    novi_broj = broj_od_cifara(cifre)
    return novi_broj

def trazeni_rezultat_za_par(par_brojeva):
    b1, b2 = par_brojeva
    # proizvod brojeva
    p1 = b1 * b2
    cifre_b1 = cifre_broja(b1)
    cifre_b2 = cifre_broja(b2)
    # p2 je proizvod cifara brojeva b1 i b2
    p2 = 1
    for c in cifre_b1:
        p2 *= c
    for c in cifre_b2:
        p2 *= c
    # zamijenimo prvu i posljednju cifru broja p2
    p2 = zamijeni_prvu_i_posljednju_cifru(p2)
    return (p1, p2)

if __name__ == '__main__':
    # za početak generišemo traženu datoteku
    datoteka = "datoteka.txt"
    donja_granica_brojeva = 3
    gornja_granica_brojeva = 99
    generisi_datoteku(naziv_datoteke=datoteka,
                      od=donja_granica_brojeva,
                      do=gornja_granica_brojeva)
    generisani_brojevi = citaj_sadrzaj_datoteke(datoteka)
    parovi_brojeva = uredjeni_parovi(generisani_brojevi)

    # otvaramo datoteku da bismo dopisali uređene parove i njihove rezultate;
    # kako trebamo dopisivati, koristimo mod 'a', odnosno 'append' √
    with open(datoteka, 'a') as f:
        f.write('\n')
        f.write('=' * 20)
        f.write('\n')
        for par in parovi_brojeva:
            trazeni_rezultat = trazeni_rezultat_za_par(par)
            f.write(str(par) + " -> " + str(trazeni_rezultat))
            f.write('\n')
