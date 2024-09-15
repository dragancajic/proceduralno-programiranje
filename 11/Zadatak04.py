'''
Data je lista stavki. U listi su date informacije o tezini svake stavke.
Dat je i proizvoljan broj korpi u koje moze stati ista kolicina stavki.
Potrebno je sve stavke smjestiti u korpe tako da se iskoristi sto manje korpi.
'''

def pakovanjeKorpi(tezineStavki, kapacitetKorpe):
    korpe = []
    preostaliKapecitetiKorpi = []

    tezineStavki.sort(reverse=True)
    
    for tezina in tezineStavki:
        for i in range(len(korpe)):
            if preostaliKapecitetiKorpi[i] >= tezina:
                preostaliKapecitetiKorpi[i] -= tezina
                korpe[i].append(tezina)
                break
        else:
            korpe.append([tezina])
            preostaliKapecitetiKorpi.append(kapacitetKorpe - tezina)

    return korpe

tezineStavki = [4, 8, 1, 4, 2, 1]
kapacitetKorpe = 10

spakovaneKorpe = pakovanjeKorpi(tezineStavki, kapacitetKorpe)
print(f"Proizvodi su spakovani u {len(spakovaneKorpe)} korpe na sljedeci nacin:")
for korpa in spakovaneKorpe:
    print(f"  {korpa}")