# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 11:25:26 2022

@author: User
"""
def rrazlike(a,b):#funkcija racunanje razlike, bira koji je broj veci i onda racuna razliku
    if a>b:
        razlika=a-b
    else:
        razlika=b-a
    return razlika
    
lista=[]#lista alfabeta malih slova
for i in range(ord('a'),ord('z')+1):
        lista.append(chr(i))
print(lista)


def specvrijednost(niska,lista):
    sumaspec=0
    for i in niska:
        if i.isupper():
            i=i.lower()
            ind=lista.index(i)
            rednibroj=ind+1
            spec=rednibroj*1.4
            sumaspec=sumaspec+spec
        elif i.islower():
            ind=lista.index(i)
            rednibroj=ind+1
            spec=rednibroj*1.6
            sumaspec=sumaspec+spec
        elif i.isdecimal():
            spec=float(i)*0.8
            sumaspec=sumaspec+spec
    return sumaspec
listaniski=[]
niska1=input()
niska2=input()
listaniski.append(niska1)
listaniski.append(niska2)
#print(specvrijednost(niska2,lista))
#print(specvrijednost(niska1,lista))
razlika=rrazlike(specvrijednost(niska2,lista),specvrijednost(niska1,lista))
#print(razlika)
    
while True:
    niska3=input()
    listaniski.append(niska3)
    #print(specvrijednost(niska3,lista))
    if specvrijednost(niska3,lista)<razlika:
        break
    razlika=rrazlike(specvrijednost(niska2,lista),specvrijednost(niska3,lista))
    #print(razlika)
    niska2=niska3

#print(listaniski)
rjecnik={}
for i in range(len(listaniski)):
    rjecnik[i]=specvrijednost(listaniski[i],lista)
print(rjecnik)

minirazlika=rrazlike(rjecnik[0],rjecnik[1])
#print(minirazlika)
indeks1=0
indeks2=1
for i in range(0,len(rjecnik)-1):
    for j in range(i+1,len(rjecnik)):
        if i==0 and j==1:
            continue
        razlika=rrazlike(rjecnik[i],rjecnik[j])
#        print(razlika)
        if razlika<minirazlika:
            minirazlika=razlika
            indeks1=i
            indeks2=j
print("Najamanja razlika je", minirazlika)
print("Indeksi su:",indeks1,indeks2)

        
        
    
