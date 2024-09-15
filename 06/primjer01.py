'''
                    ---Rad sa datotekama---
'''

# otvaranje datoteke, sintaksa:
# open(putanjaDoDatoteke, nacinRada)

# razlikujemo tri načina rada:
    # "r" - čitanje sadržaja iz datoteke
    # "w" - upisivanje sadržaja u datoteku
    # "a" - dopisivanje sadržaja u datoteku

file = open("ulaz.txt", "r", encoding='utf-8')

sadrzaj = file.read()
print(sadrzaj)

# metod `read()` ČITA SVE KARAKTERE iz datoteke !!!

file.close()
# nakon što završimo sa radom, potrebno je zatvoriti datoteku!
