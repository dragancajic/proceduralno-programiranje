'''
                    ---Operacije nad listama---
'''

L1 = [1, 2, 3, 4, 5]
L2 = [10, 9, 8, 7, 6]

print("L1 * 2:", L1 * 2)
print("L1 + L2:", L1 + L2)
print("-" * 60)

L3 = L1 + L2
print("L3:", L3)

print("Sortirana lista L3:", sorted(L3))
print("Najveci element u listi L3:", max(L3))
print("Najmanji element u listi L3:", min(L3))
print("Suma elementa u listi L3:", sum(L3))
print("-" * 60)

print("L3:", L3)

print("-" * 60)
# operator `in` - provjerava da li je neki element prisutan u listu
print("5 in L3:", 5 in L3)
print("100 in L3:", 100 in L3)
