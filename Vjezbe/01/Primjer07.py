#                           ---Rad sa stringovima--

a = "Dobar dan svima. Kako ste?"
print(a)

# len(a) - vraća dužinu stringa a
print("Duzina stringa a:", len(a))

# a[i] - ispisuje i-to slovo stringa a
print("7. slovo stringa a:", a[7])

# a[i:j] - ispisuje karaktere počev od i-tog, bez j-tog karaktera
print("a[2:7] ->", a[2:7])

# Neke korisne metode
print(a.upper())            # sva slova velika
print(a.lower())            # sva slova mala
print(a.replace("a", "t"))  # zamjena karaktera
print(a.replace("ste", "si"))
print("Broj pojavljivanja karaktera 'o' je:", a.count("o"))
# Više o `str`-ing metodama u Pajtonu možete pronaći na:
# https://www.w3schools.com/python/python_ref_string.asp
print("--------------------------------------")

# Operacije sa stringovima
prvi = "Zdravo"
drugi = "svijete!"

zajedno = prvi + drugi
print(zajedno)
zajedno = prvi + " " + drugi
print(zajedno)
print("--------------------------------------")

visePuta = prvi * 5
print(visePuta)
