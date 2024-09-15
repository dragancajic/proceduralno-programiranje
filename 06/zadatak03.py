# U datoteci `filmovi.txt` se u svakom redu nalazi infomacija o nazivu filma i
# ocjeni koju je on dobio od nekog kritičara. Napisati program koji u datoteku
# `prosjecneOcjene.txt` upisuje film i njegovu prosječnu ocjenu.

def prosjecnaOcjena(listaOcjena):
    return sum(listaOcjena) / len(listaOcjena)

filmovi = {}

# učitavamo filmove i njigove ocjene u rječnik;
# formiramo rječnik tako da su ključevi filmovi,
# a vrijednosti liste ocjena filmova
with open ("filmovi.txt", "r") as inputFile:
    for line in inputFile:
        film, ocjena = line.split(" : ")
        ocjena = int(ocjena)

        if film in filmovi:
            filmovi[film].append(ocjena)
        else:
            filmovi[film] = [ocjena]
        #print(filmovi)

for i, film in enumerate(filmovi):
    print(i+1, film, filmovi[film])

# upisujemo filmove i njihove prosječne ocjene u datoteku
# `prosjecneOcjene.txt`
with open("prosjecneOcjene.txt", "w") as outputFile:
    for film in filmovi:
        ocjene = filmovi[film]
        prosjecnaOcjenaFilma = prosjecnaOcjena(ocjene)
        outputFile.write(f"{film} : {round(prosjecnaOcjenaFilma, 2)}\n")

print("Upisivanje zavrseno!")
