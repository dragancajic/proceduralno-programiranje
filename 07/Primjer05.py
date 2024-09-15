
#Sintaksa: filter(f, sequence) 
#gdje je "f" mora da vrati logicku vrijednost (True ili False)

#ispisati samo one rijeci koje sadrze malo slovo "p"
rijeci = ["kolokvijum", "ispit", "polaganje", "ocjena", "bodovi"]

sadrzeP = list(filter(lambda rijec: rijec.__contains__("p"), rijeci))
print("Rijeci koje sadrze malo slovo \"p\":", sadrzeP)