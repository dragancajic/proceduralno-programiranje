'''
                    ---Upisivanje sadržaja u datoteku---
                    ---Уписивање садржаја у датотеку---

Sa tastature se unose/učitavaju rečenice sve dok korisik ne unese
riječ `stop`. Unesene rečenice je potrebno upisati u datoteku
`recenice.txt`.

Са тастатуре се уносе/учитавају реченице све док корисник не унесе
ријеч `stop`. Унесене реченице је потребно уписати у датотеку
`recenice.txt`.
'''

with open("recenice.txt", "w", encoding='utf-8') as outputFile:
    while True:
        recenica = input("Unesite recenicu ili \"stop\" za prekid: ")

        if recenica == "stop":
            break

        outputFile.write(recenica)
        outputFile.write("\n")

print("Upisivanje u datoteku zavrseno.")
