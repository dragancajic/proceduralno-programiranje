'''
Napisati funkciju koja pronalazi godine izbora u zvanje saradnika u nastavi
i ispisuje ih na standardnom izlazu sortirane u opadajućem poretku.
'''

import re

def pronadji_i_sortiraj(datoteka):
    '''pronadji i sortiraj saradnike u nastavi'''
    with open(datoteka, encoding='utf-8') as ulaz:
        tekst = ulaz.read()
    sablon = re.compile(r"\d{4}")
    godine = sablon.findall(tekst)
    # Metod `findall()` pronalazi sve podudarajuće podniske
    # u tekstu i vraća ih kao listu.
    # Ako "uzorak" nije pronađen, vraća se prazna lista.
    godine.sort(reverse=True)
    return godine

DATOTEKA = input("Unesite naziv datoteke: ")
GODINE = pronadji_i_sortiraj(DATOTEKA)
print("Godine izbora u zvanje:", ", ".join(GODINE))
