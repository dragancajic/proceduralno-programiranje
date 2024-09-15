'''
Problem razmjenjivanja novca:
Potrebno je razmjeniti zadatu kolicinu novca koristeci
novcacnice od 1, 2, 5, 10, 20, 50, 100 i 200 KM
tako da se upotrijebi sto manje novcanica.
'''

def najmanjiBrojNovcanica(kolicinaNovca):
    novcanice = [1, 2, 5, 10, 20, 50, 100, 200]

    rjesenje = []
    i = len(novcanice) - 1  #krecemo od novcanice na posljednjoj poziciji
                            #tj. "najvece" novcanice
                            #pretpostavlja se da je lista novcanica sortirana

    while(i >= 0):
        trenutnaNovcanica = novcanice[i]
        brojTrenutnihNovcanica = kolicinaNovca // trenutnaNovcanica

        kolicinaNovca -= trenutnaNovcanica * brojTrenutnihNovcanica
        rjesenje += brojTrenutnihNovcanica * [trenutnaNovcanica]
        
        i -= 1 #prelazimo na sljedecu novcanicu

    return rjesenje

novac = int(input("Unesite kolicinu novca:"))
razmjenjeno = najmanjiBrojNovcanica(novac)

print(f"{novac} = ", end="")
print(' + '.join(map(str, razmjenjeno)))