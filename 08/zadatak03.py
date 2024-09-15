'''
Napisati funkciju koja u učitanoj datoteci mijenja format
u kom su zapisani podaci o studentu.

Na primjer, datoteka:
```
162/2018, Dorotea Pavlović
28/2019, Filip Ristić
413/2019, Jelena Petrović
```
se mijenja u:
```
18/162, Pavlović Dorotea
19/28, Ristić Filip
19/413, Petrović Jelena
```
'''

import re

def izmijeni_dokument(dokument):
    '''izmijeni dokument'''
    with open(dokument, "r+", encoding="UTF-8") as fajl:
        tekst = fajl.read()
        sablon = re.compile(r"(\d{1,4})/\d{2}(\d{2}),\s+(\w+)\s+(\w+)")

        novi_tekst = sablon.sub(r"\2/\1, \4 \3", tekst)
        # Metod `sub()` se koristi za izvršavanje zamena u teksta na osnovu
        # zadatog regularnog izraza. Kada pronađe podudaranje "uzorka", ona
        # ga zamenjuje navedenim zamenskim tekstom.
        fajl.seek(0)            # vraćamo se na početak
        fajl.truncate()         # uklanjamo postojeći zadržaj datoteke
        fajl.write(novi_tekst)  # upisujemo novi tekst u datoteku

datoteka = input("Unesite naziv datoteke: ")
izmijeni_dokument(datoteka)
