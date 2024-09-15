#Napisati fukciju koja za argument uzima neku rijec, a kao rezultat vraca listu svih
#permutacija te rijeci

def permutacijeRijeci(rijec):
    #bazni slucaj: ako je string prazan ili ako ima samo jedan karakter
    #vracamo listu u kojoj je samo taj karakter
    if len(rijec) <= 1:
        return [rijec]
    
    #prazna lista za cuvanje permutacija
    permutacije = []
    
    #prolazimo kroz svaki karakter stringa
    for i in range(len(rijec)):
        #fiksiramo jedan (trenutni) karakter kao prvi karakter 
        #i kreiramo permutacije preostalih karaktera
        fiksiraniKarakter = rijec[i]
        ostatakRijeci = rijec[:i] + rijec[i+1:]
        permutacijeOstatkaRijeci = permutacijeRijeci(ostatakRijeci)
        
        #dodajemo fiksirani karakter svakoj permutaciji preostalih karaktera
        for permutacija in permutacijeOstatkaRijeci:
            permutacije.append(fiksiraniKarakter + permutacija)
    
    return permutacije

rijec = "abcd"
permutacije = permutacijeRijeci(rijec)
print(f"Rijec \"{rijec}\" ima {len(permutacije)} permutacija. Te permutacije su:\n  {permutacije}")