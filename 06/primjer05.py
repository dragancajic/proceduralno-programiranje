'''
~ Primjer 5 ~

file.readlines() <-- чита СВЕ ЛИНИЈЕ ДАТОТЕКЕ и смјешта их у листу!
'''

file = open("ulaz.txt", "r", encoding='utf-8')

linije = file.readlines()
# metod `readlines()` čita sve linije datoteke i smješta ih u listu

print("Dobijena je lista:", linije)

print("\nPrikaz sadrzaja datoteke:\n")
for linija in linije:
    print(linija, end="")

file.close()
