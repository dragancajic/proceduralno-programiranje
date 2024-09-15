# U datoteci `grupa1.txt` nalaze se ostvareni bodovi studenata koji su ispit
# polagali u prvoj grupi, dok se u datoteci `grupa2.txt` nalaze ostvareni
# bodovi studenata koji su ispit polagali u drugoj grupi. Napisati program
# koji će u datoteku `ispit.txt` upisati infromacije o svim studentima koji
# su polagali ispit. Prve linije datoteka `grupa1.txt` i `grupa2.txt` se ne
# upisuju u datoteku `ispit.txt`.

with open("grupa1.txt", "r") as grupa1, \
     open("grupa2.txt", "r") as grupa2, \
     open("ispit.txt", "w") as ispit:
    ispit.write("Rezultati ispita:\n")

    grupa1.readline()  # čitamo prvu liniju datoteke "grupa1.txt",
                       # ali ne radimo ništa sa njom!

    # ostale linije upisujemo u datoteku "ispit.txt"
    for line in grupa1:
        ispit.write(line.strip())
        ispit.write("\n")

    grupa2.readline()  # čitamo prvu liniju datoteke "grupa2.txt",
                       # ali ne radimo ništa sa njom!

    # ostale linije uspisujemo u datoteku "ispit.txt"
    for line in grupa2:
        ispit.write(line.strip())
        ispit.write("\n")

print("Upisivanje zavrseno!")
