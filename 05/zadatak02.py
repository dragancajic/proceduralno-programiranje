'''
Sa tastature se unosi rečenica.
Za svaku riječ unesene rečenice ispisati koliko se puta ona pojavljuje
u rečenici. Ne praviti razliku između malih i velikih slova.
Napomena: Pretpostaviti da unesene rečenica ne sadrži znakove interpunkcije.
'''

recenica = input("Unesite recenicu: ")
recenica = recenica.lower()  # prebacujemo sve u mala slova

rijeci = recenica.split(" ")
print("Rijeci koje se nalaze u unesenoj recenici:", rijeci)
print()

# brojPojavljivanjaRijeci = dict()
brojPojavljivanjaRijeci = {}

for rijec in rijeci:
    if rijec in brojPojavljivanjaRijeci:
        # operator `in` provjerava da li se odgovarajući ključ
        # nalazi unutar rječnika
        brojPojavljivanjaRijeci[rijec] += 1
    else:
        brojPojavljivanjaRijeci[rijec] = 1

# for rijec in brojPojavljivanjaRijeci:
#     print(f"Rijec \"{rijec}\" se u recenici pojavljuje {brojPojavljivanjaRijeci[rijec]} puta.")

for rijec, pojavljivanje in brojPojavljivanjaRijeci.items():
    print(f"Rijec \"{rijec}\" se u recenici pojavljuje {pojavljivanje} puta.")
