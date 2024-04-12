# Sa tastature se unosi prirodan broj koji predstavlja broj godina neke osobe.
# Na ekranu je potrebno ispisati informaciju o tome da li je ta osoba punoljetna
# ili ne.

godine = int(input("Unesite broj godina: "))

if godine < 0:
    print("Broj godina ne moze biti negativan broj.")
elif godine >= 18:
    print("Osoba je punoljetna.")
else:
    print("Osoba nije punoljetna.")
