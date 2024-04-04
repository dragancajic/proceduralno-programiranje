#                   ---Upisivanje sadržaja u datoteku---

# Sa tastature se unose/učitavaju rečenice sve dok korisik ne unese
# riječ `stop`. Unesene rečenice je potrebno upisati u datoteku
# `recenice.txt`.

with open("recenice.txt", "w") as outputFile:
    while (True):
        recenica = input("Unesite recenicu ili \"stop\" za prekid: ")

        if recenica == "stop":
            break

        outputFile.write(recenica)
        outputFile.write("\n")

print("Upisivanje u datoteku zavrseno.")
