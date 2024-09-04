'''
                    ---Metode na skupovima---
'''

A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 7, 8}

print("A:", A)
print("B:", B)

print("-" * 40)

unija = A.union(B)
print("A ∪ B:", unija)

presjek = A.intersection(B)
print("A ∩ B:", presjek)

razlika = A.difference(B)
print("A \ B:", razlika)

simetricnaRazlika = A.symmetric_difference(B)
print("A ∆ B:", simetricnaRazlika)

# više o metodama nad skupovima možete pronaći na:
# https://www.w3schools.com/python/python_ref_set.asp

# ∪ - union                <=> operator `|`   <-- УНИЈА
# ∩ - intersection         <=> operator `&`   <-- ПРЕСЈЕК
# \ - difference           <=> operator `-`   <-- РАЗЛИКА СКУПОВА `A\B`
# ∆ - symmetric difference <=> operator `^`   <-- СИМЕТРИЧНА РАЗЛИКА,
# односно КОМПЛЕМЕНТ ПРЕСЈЕКА
