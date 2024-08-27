'''
                        ---Rad sa stringovima--
'''

A = "Dobar dan svima. Kako ste?"
print(A)

# len(A) - vraća dužinu stringa A
print("Duzina stringa A:", len(A))

# A[i] - ispisuje i-to slovo stringa A
print("7. slovo stringa A:", A[7])

# A[i:j] - ispisuje karaktere počev od i-tog, bez j-tog karaktera
print("A[2:7] ->", A[2:7])

# Neke korisne metode
print(A.upper())            # sva slova velika
print(A.lower())            # sva slova mala
print(A.replace("a", "t"))  # zamjena karaktera
print(A.replace("ste", "si"))
print("Broj pojavljivanja karaktera 'o' je:", A.count("o"))
# Više o `str`-ing metodama u Pajtonu možete pronaći na:
# https://www.w3schools.com/python/python_ref_string.asp
print("--------------------------------------")

# Operacije sa stringovima
PRVI = "Zdravo"
DRUGI = "svijete!"

ZAJEDNO = PRVI + DRUGI
print(ZAJEDNO)
ZAJEDNO = PRVI + " " + DRUGI
print(ZAJEDNO)
print("--------------------------------------")

VISE_PUTA = PRVI * 5
print(VISE_PUTA)
