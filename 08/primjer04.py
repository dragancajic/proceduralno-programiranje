'''
                    ---Metod finditer()---
'''

import re

sablon = re.compile(r"dan")
TEKST = "danas je divan dan"

for e in sablon.finditer(TEKST):
    print(e)

# Metod `finditer()` pronalazi sve podudarajuće podniske u tekstu
# i vraća ih kao iterator koji sadrži podudarajuće objekte.

# izlaz:
# <re.Match object; span=(0, 3), match='dan'>
# <re.Match object; span=(15, 18), match='dan'>
