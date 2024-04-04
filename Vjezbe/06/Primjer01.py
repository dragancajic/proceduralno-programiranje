#                           ---Rad sa datotekama---

# otvaranje datoteke, sintaksa:
# open(putanjaDoDatoteke, nacinRada)

# razlikujemo tri načina rada:
    # "r" - čitanje sadržaja iz datoteke
    # "w" - upisivanje sadržaja u datoteku
    # "a" - dopisivanje sadržaja u datoteku

file = open("ulaz.txt", "r")

sadrzaj = file.read()
print(sadrzaj)

# metod `read()` čita sve karaktere iz datoteke

file.close()
# nakon što završimo sa radom, potrebno je zatvoriti datoteku!
