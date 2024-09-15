#                                           ---Lambda funkcije---

# Lambda funkcije: anonimne funkcije
# Sintaksa y = lambda arg1, arg2,...: izraz
# poziv: y(vr1, vr2,...)

f = lambda a, b: a * b

print("f(2, 3):", f(2, 3))

#Karakteristike Lambda funkcija u Pajtonu:
    #Lambda funkcije mogu da imaju vise argumenata ali vracaju samo jednu vrijednost.
    #Lambda funkcije se pisu u jednom redu i stoga ne mogu sadrzavati viselinijske izraze.
    #Lambda izrazi mogu biti argumenti za druge funkcije.
    #Lambda funkcije nemaju eksplicitno naveden return iskaz
