file = open("ulaz.txt", "r")

linije = file.readlines()
# metod `readlines()` čita sve linije datoteke i smješta ih u listu

print("Dobijena je lista:", linije)

print("\nPrikaz sadrzaja datoteke:\n")
for linija in linije:
    print(linija, end="")

file.close()
