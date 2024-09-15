import re
import sys
import getopt

def prosjecna_cijena(br,lista):
    prosjecna=0
    brojac=0
    for k in lista:
        if k["naziv"]==br:
            prosjecna+=k["cijena"]
            brojac+=1
    return prosjecna/brojac



argumenti=sys.argv[1:]
try:
    o,a = getopt.getopt(argumenti,"i:o:z:")
except getopt.GetoptError:
    print("greska pri unosu!")
    exit(1)
ulazni_fajl=""
izlazni_fajl=""
zadatak=""

for x,y in o:
    if x=="-i":
        ulazni_fajl+=y
    elif x=="-o":
        izlazni_fajl+=y
    elif x=="-z":
        zadatak+=y
    else:
        print("greska pri unosu!")
        exit(1)

f1=open(ulazni_fajl,"r")
pattern=re.compile(r"([a-zA-Z]+),\s+"r"(\w+\s*\w*)+:\s+"r"(\d+)")
lista_telefona=[]
for k in f1:
    telefoni={}
    for i in pattern.finditer(k):
        naziv_telefona=i.group(1)
        tip_telefona=i.group(2)
        cijena_telefona=i.group(3)
        telefoni["naziv"]=naziv_telefona
        telefoni["tip"]=tip_telefona
        telefoni["cijena"]=int(cijena_telefona)
    lista_telefona.append(telefoni.copy())
f1.close()

if zadatak=="1":
    f1=open(izlazni_fajl,"w")
    for k in lista_telefona:
        if k["cijena"]>400:
            f1.write(k["naziv"]+"\n")
    f1.close()
elif zadatak=="2":
    f1=open(izlazni_fajl,"w")
    for k in lista_telefona:
        if k["cijena"]>100 and k["cijena"]<300:
            f1.write(k["tip"]+"\n")
    f1.close()
elif zadatak=="3":
    f1=open(izlazni_fajl,"w")
    provjera=[]
    for k in lista_telefona:
        if prosjecna_cijena(k["naziv"],lista_telefona)<401:
            if k["naziv"] not in provjera:
                f1.write(k["naziv"]+"\n")
                provjera.append(k["naziv"])         
    f1.close()
else:
    print("pogresan unos")
    exit(1)