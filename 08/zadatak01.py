'''
Sa tastature se unose tekst i riječ.
Napisati program koji ispisuje indekse pojavljivanja riječi u tekstu.
'''

import re

tekst = input("Unesite tekst: ")
rijec = input("Unesite rijec: ")

sablon = re.compile(rijec)

print(f"Rijec \"{rijec}\" se u tekstu\n\"{tekst}\"\n pojavljuje na pozicijama:")
for pogodak in sablon.finditer(tekst):
    print(pogodak.start(), end=" ")

print()
