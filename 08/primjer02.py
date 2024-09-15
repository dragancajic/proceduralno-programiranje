'''
                    ---Metod match()---
'''

import re

sablon1 = re.compile(r"Dan")
sablon2 = re.compile(r"divan")
TEKST = "Danas je divan dan"

print(sablon1.match(TEKST))
print(sablon2.match(TEKST))

# Metod `match()` traži odgovarajući "uzorak" samo na početku niske.

# izlaz:
# <re.Match object; span=(0, 3), match='Dan'>
# None
