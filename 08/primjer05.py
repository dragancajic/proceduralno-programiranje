'''
Metode `start()`, `end()` i `span()` vraćaju
informacije o poziciji pogotka unutar stringa.
'''

import re

sablon = re.compile(r"ovu")
TEKST = "pronadji ovu rijec"

pogodak = sablon.search(TEKST)

if pogodak:
    pocetak = pogodak.start()
    print("Pocetak:", pocetak)
    kraj = pogodak.end()
    print("Kraj:", kraj)
    span = pogodak.span()
    print("Span:", span)

# izlaz:
# Pocetak: 9
# Kraj: 12
# Span: (9, 12)
