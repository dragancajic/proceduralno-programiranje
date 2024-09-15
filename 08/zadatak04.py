'''
U datoteci "automobili.txt" u svakom redu zapisane su sljedeće informacije:
```marka, model: cijena```
Napisati Pajton skriptu koja treba da se pokrene iz terminala sa opcijama
    -i (--Input): koja zadaje ulaznu datoteku koja treba da bude
        ucitana u program;
    -t (--Task): koja zadaje zadatak koji treba da bude izvršen, i obuhvata
        sljedeće vrijednosti:
            1: na ekran treba da se ispišu sve marke automobila koje su luksuzne.
               Marka automobila je luksuzna ako postoji barem jedan njegov model
               sa cijenom većom od 30000.
            2: na ekran treba da se ispišu svi automobila sa cijenom
               manjom od k (k se unosi sa tastature)
            za ostale vrijednosti javiti grešku o neispravnom zadatku.
'''

import getopt
import sys

def procitaj_automobile(putanja_do_automobila):
    '''procitaj datoteku s automobilima'''
    linije = []
    with open(putanja_do_automobila, "r", encoding='utf-8') as ulaz:
        for linija in ulaz:
            linija = linija.strip()
            linija = linija.replace(":", ",")
            linije.append(linija)

    return linije

def pronadji_luksuzne_marke(lista_automobila):
    '''pronajdi luksuzne marke automobila'''
    luksuzne_marke = set()
    for automobil in lista_automobila:
        info = automobil.split(",")
        if int(info[2]) >= 30000:
            luksuzne_marke.add(info[0].strip())

    return luksuzne_marke

def jeftiniji_od(lista_automobila, cijena):
    '''pronadji jeftinije automobile od date cijene'''
    jeftinija_auta = set()
    for automobil in lista_automobila:
        info = automobil.split(",")
        if int(info[2]) < cijena:
            jeftinija_auta.add(info[0].strip() + " - " + info[1].strip())

    return jeftinija_auta

argumenti = sys.argv[1:]

OPCIJE = "i:t:"
dugacke_opcije = ["Input=", "Task="]

ULAZNA_DATOTEKA = None
ZADATAK = None

try:
    OPCIJE, _ = getopt.getopt(argumenti, OPCIJE, dugacke_opcije)
except getopt.GetoptError as err:
    print(str(err))

if len(OPCIJE) != 2:
    print("Pozivanje programa:\n\tzadatak04.py -i <inputFile> -t task(1 or 2)")
    sys.exit()

for opcija, vrijednost in OPCIJE:
    if opcija in ("-i", "--Input"):
        ULAZNA_DATOTEKA = str(vrijednost)
    elif opcija in ("-t", "--Task"):
        if vrijednost not in ('1', '2'):
            sys.exit("Task opcija moze biti samo 1 ili 2")
        ZADATAK = int(vrijednost)

automobili = procitaj_automobile("automobili.txt")
#print(automobili)
# [
#     'Volkswagen, Golf 7, 12000',
#     'Porsche, Carrera , 100000',
#     'Toyota, Supra, 45000',
#     'Volkswagen, Golf 6, 6000',
#     'Porsche, 911 , 130000',
#     'Volkswagen, Golf 8, 30000',
#     'Citroen, C4, 5000'
# ]

if ZADATAK == 1:
    print("Luksuzne marke automobila:", pronadji_luksuzne_marke(automobili))
elif ZADATAK == 2:
    k = float(input("Unesite cijenu: "))
    print(f"Automobili sa cijenom manjom od {k}: {jeftiniji_od(automobili, k)}")

# Pokretanje:
# python zadatak04.py -i automobili.txt -t 1
# ili
# python zadatak04.py -i automobili.txt -t 2
