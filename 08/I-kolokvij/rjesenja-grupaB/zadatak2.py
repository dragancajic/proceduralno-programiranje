def prost(br):
    if br == 1:
        return False
    for k in range(2,br//2+1):
        if br%k==0:
            return False
    return True
def broj_prosti_faktori(br):
    brojac=0
    for k in range(2,br):
        if prost(k) and br%k==0:
            brojac+=1
    return brojac
def suma_slozenih_djelilaca(lista):
    suma=0
    for k in lista:
        for br in range(1,k+1):
            if prost(br)==False and k%br==0:
                suma+=br
    return suma

lista_brojac2=[]
brojac2=0
brojac1=0
uslov1=True
uslov2=True
lista=[]
while uslov1:
    if brojac1==4:
        break
    else:
        brojac1=0
    pomocna_lista=[]
    uslov2=True
    while uslov2:
        if brojac2==9:
            lista_brojac2=[]
            brojac2=0
            uslov2=False
        else:
            x=int(input("unesite broj:"))
            if x not in lista_brojac2:
                brojac2+=1
            if prost(x):
                brojac1+=1
            lista_brojac2.append(x)
            pomocna_lista.append(x)
    lista.append(pomocna_lista.copy())
print("lista:")
print(lista)

lista_sortirana1=[]
for k in lista:
    k=sorted(k,key=broj_prosti_faktori)
    lista_sortirana1.append(k)


lista_sortirana2=sorted(lista_sortirana1,key=suma_slozenih_djelilaca)
print("sortirana lista:")
print(lista_sortirana2)