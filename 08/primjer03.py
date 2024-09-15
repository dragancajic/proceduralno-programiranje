'''
                    ---Metod search()---
'''

import re

sablon1 = re.compile(r"Dan")
sablon2 = re.compile(r"divan")
TEKST = "Danas je divan dan"

print(sablon1.search(TEKST))
print(sablon2.search(TEKST))

# Metod `search()` traži odgovarajući "uzorak" u cijeloj niski.

# izlaz:
# <re.Match object; span=(0, 3), match='Dan'>
# <re.Match object; span=(9, 14), match='divan'>
