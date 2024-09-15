'''
Napisati skriptu koja uzima dva argumenta, `-i` (ili duže `--Input`) za ulaznu
datoteku i `-o` (ili duže `--Output`) za izlaznu datoteku.
U slučaju da korisnik ne proslijedi obavezne argumente, skripta treba da ispiše
poruku o grešKi.
Na kraju, sadržaj ulazne datoteke je potrebno prepisati u izlaznu datoteku.
'''

import getopt
import sys

argumenti = sys.argv[1:]

OPCIJE = "hi:o:"
dugacke_opcije = ["Help", "Input=", "Output="]

ULAZNA_DATOTEKA = None
IZLAZNA_DATOTEKA = None

try:
    OPCIJE, _ = getopt.getopt(argumenti, OPCIJE, dugacke_opcije)
except getopt.GetoptError as err:
    print(str(err))

if len(OPCIJE) != 2:
    sys.exit("Nekorektan poziv programa!")

for opcija, vrijednost in OPCIJE:
    if opcija in ("-h", "--Help"):
        print("primjer08.py -i <inputFile> -o <outputFile>")
    elif opcija in ("-i", "--Input"):
        print("Ulazna datoteka:", vrijednost)
        ULAZNA_DATOTEKA = str(vrijednost)
    elif opcija in ("-o", "--Output"):
        print("Izlazna datoteka:", vrijednost)
        IZLAZNA_DATOTEKA = str(vrijednost)

try:
    with open(ULAZNA_DATOTEKA, "r", encoding='utf-8') as ulaz, \
         open(IZLAZNA_DATOTEKA, "w", encoding='utf-8') as izlaz:
        for line in ulaz:
            izlaz.write(line)
except FileNotFoundError:
    print(f"Greska prilikom otvaranja datoteke \"{ULAZNA_DATOTEKA}\".")
else:
    print("Prepisivanje zavrseno!")

# Pokretanje:
# python primjer08.py -i ulaz.txt -o izlaz.txt
