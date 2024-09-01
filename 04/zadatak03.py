'''
Sa tastature se unose brojevi sve dok se ne unese broj
koji je veći od sume dva prethodno unesena broja.
Kreirati listu listi prostih djelilaca unesenih brojeva.
Broj unesenih brojeva mora biti bar tri.
'''

def prost(n):
    '''
    provjeri da li je broj prost
    '''
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def prosti_faktori(n):
    '''
    odredi proste faktore broja / djelioce koji su prosti brojevi
    '''
    lista_prostih_faktora = []
    for i in range(2, n+1):
        if(n % i == 0 and prost(i)):
            lista_prostih_faktora.append(i)

    return lista_prostih_faktora

    #return [faktor for faktor in range(2, n+1) if prost(faktor) and n % faktor == 0]
    # -- ekvivalentno dijelu koda od #22. do #25. linije

brojevi = []
b1 = int(input("Unesite prvi broj: "))
brojevi.append(b1)
b2 = int(input("Unesite drugi broj: "))
brojevi.append(b2)
b3 = int(input("Unesite treci broj: "))
brojevi.append(b3)

while b3 <= b1 + b2:
    b1, b2 = b2, b3  # b1 = b2; b2 = b3
    b3 = int(input("Unesite novi broj: "))
    brojevi.append(b3)

matricaProstihFaktora = []
for broj in brojevi:
    matricaProstihFaktora.append(prosti_faktori(broj))

#matricaProstihFaktora = [prosti_faktori(k) for k in brojevi]
# - ekvivalentno dijelu koda od #45. do #47. linije

print("Broj : Prosti faktori")
for broj, listaProstihFaktora in zip(brojevi, matricaProstihFaktora):
    print(f"{broj:4} : {listaProstihFaktora}")
