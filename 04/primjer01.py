'''
                    ---Liste---

Lista je jedna od osnovnih struktura podataka u Pajtonu.
Lista predstavlja uređen, promenljivi skup elemenata,
kojima se može pristupiti po indeksu.
U listama je moguće čuvati različite vrste podataka.
'''

# L = []      # prazna lista
# L = list()  # prazna lista

L = [1, 2, 3, 4, 5, "a", "b", "c", True, 5.12]
print("L:", L)

# pristup elementima liste: `nazivListe[indeksZeljenogElementa]`
print(f"Prvi element liste {L} je {L[0]}.")
print(f"Sedmi element liste {L} je {L[6]}.")
print(f"Posljednji element liste {L} je {L[-1]}")

# podliste
print("-" * 80)

print("L:", L)
print("L[0:3]:", L[0:3])
print("L[0:5:2]:", L[0:5:2])
print("L[::2]", L[::2])
print("L[2::2]", L[2::2])
print("L[:7:3]:", L[:7:3])
print("L[::-1]:", L[::-1])

print("-" * 80)
# izmjena elemenata u listu
print("Lista prije izmjene:", L)
L[8] = False  # moze i `L[-2] = False`
print("Lista nakon izmjene:", L)
