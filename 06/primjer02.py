"""
~ Primjer 2 ~

file.read(size) <-- LOOK! читање задатог БРОЈа КАРАКТЕРА користећи `size`
"""

file = open("ulaz.txt", "r", encoding='utf-8')

sadrzaj = file.read(10)  # čitamo prvih 10 karaktera iz fajla
print(sadrzaj)

sadrzaj = file.read(10)  # čitamo narednih 10 karaktera iz fajla
print(sadrzaj)

file.close()
