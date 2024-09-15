#                                           ---Izuzetci---

try:
    with open("datoteka.txt", "r") as ulaznaDatoteka:
        for line in ulaznaDatoteka:
            print(line, end="")
        print()
except FileNotFoundError:
    #dio koda koji se izvrsava u slucaju da se baci izuzetak
    print("Nije moguce otvoriti datoteku.")
else:
    #dio koda koji se izvrsava u slucaju da se ne baci izuzetak
    print("Ovaj dio koda se izrsava ako se ne baci izuzetak.")
finally:
    #dio koda koji se izvrsava bez obzira na to da li je bacen izuzetak
    print("Ovaj dio koda se izvrsava bez obriza na to da li ce se baciti izuzetak ili ne.")