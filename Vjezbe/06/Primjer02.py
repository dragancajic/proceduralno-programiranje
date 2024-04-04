file = open("ulaz.txt", "r")

sadrzaj = file.read(10)  # čitamo prvih 10 karaktera iz fajla
print(sadrzaj)

sadrzaj = file.read(10)  # čitamo narednih 10 karaktera iz fajla
print(sadrzaj)

file.close()
