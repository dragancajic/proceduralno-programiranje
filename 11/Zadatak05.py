'''
Napisati fuknciju koja pronalazi najmanji broj sa zadatim brojem cifara
i sa zadatom sumom cifara.
'''

def konvertujUBroj(nizCifara):
    broj = 0
    for cifra in nizCifara:
        broj *= 10
        broj += cifra
    
    return broj

#funkcija koja pronalazi broj koji ima "brojCifara" cifara i cija je 
#suma cifara "sumaCifara"
def najmanjiBroj(brojCifara, sumaCifara):
    if brojCifara <=0 or sumaCifara < 0:
        exit("Nekorektan unos broja cifara i sume cifara.")
    #jedini broj sa sumom cifara 0 je 0
    if sumaCifara == 0:
        if brojCifara == 1:
            return 0
        else:
            exit(f"Broj koji ima {brojCifara} cifara takav da mu je suma cifara"
             f" {sumaCifara} ne postoji.")
            
    #broj ce imati najvecu sumu cifara ako se sastoji samo od devetki
    #ako je data suma cifara veca od najvece moguce, onda takav broj ne postoji
    if(sumaCifara > 9 * brojCifara):
        exit(f"Broj koji ima {brojCifara} cifara takav da mu je suma cifara"
             f" {sumaCifara} ne postoji.")

    #postavimo da su napocetku sve cifre broja nule    
    cifreBroja = [0] * brojCifara

    #posto prva cifra broja ne moze biti nula od sume cifara oduzimamo jedinicu
    #tu jedinicu cemo ponovo dodati kada budemo postavljali cifru najveceg znacaja
    sumaCifara -= 1

    #popunjavamo redom cifre od cifre najmanjeg znacaja do cifre
    #najveceg znacaja
    for i in range(brojCifara - 1, 0, -1):
        if sumaCifara > 9:
            cifreBroja[i] = 9
            sumaCifara -= 9
        else:
            cifreBroja[i] = sumaCifara
            sumaCifara = 0
    cifreBroja[0] = sumaCifara + 1

    return konvertujUBroj(cifreBroja)

brojCifara = int(input("Unesite broj cifara broja:"))
sumaCifara = int(input("Unesite sumu cifara broja:"))

broj = najmanjiBroj(brojCifara, sumaCifara)
print(f"Najmanji broj koji ima {brojCifara} cifara i cija je suma cifara"
             f" {sumaCifara} je: {broj}.")