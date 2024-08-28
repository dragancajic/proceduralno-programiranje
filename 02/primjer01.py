'''
                    ---Relacioni i logički operatori---
'''

# Operatori poređenja (relacioni operatori):
    # manje             - `<`
    # manje ili jednako - `<=`
    # veće              - `>`
    # veće ili jednako  - `>=`
    # jednakost         - `==`
    # nejednakost       - `!=`

# Logički operatori:
    # konjukcija        - `and`
    # disjunkcija       - `or`
    # negacija          - `not`

# Aritmetički operatori imaju veći prioritet u odnosu na relacione operatore!
# Relacioni operatori imaju veći prioritet u odnosu na logičke operatore. √
# Relacioni operatori imaju isti prioritet između sebe. √ LOOK! :eyes:

print("3 < 5:", 3 < 5)                                      # True
print("3 < 5 != False:", 3 < 5 != False)                    # True
print("(3 < 5) and (5 != True):", (3 < 5) and (5 != True))  # True
print("-" * 30)

# Ukoliko je vrijednost prvog operanda `True` i ako se vrši logička operacija
# `or` Pajton automatski vraća `True` bez obzira na vrijednost drugog operanda.
print("(2 < 3) or (1 / 0):", (2 < 3) or (1 / 0))    # True √

# Ukoliko je vrijednost prvog operanda `False` i ako se vrši logička operacija
# `and` Pajton automatski vraća `False` bez obzira na vrijednost drugog operanda.
print("(5 < 3) and (1 / 0):", (5 < 3) and (1 / 0))  # False √
print("-" * 30)

# Poređenje slova - ASCII kôd
print("'A' < 'Z':", 'A' < 'Z')            # True
print("'a' < 'Z':", 'a' < 'Z')            # False
print("'abc' < 'abd':",'abc' < 'abd')     # True
print("'abc' == 'abc':", 'abc' == 'abc')  # True
print("'ABC' == 'abc':", 'ABC' == 'abc')  # False
print("-" * 30)

# operator `in`
print ("'Jan' in '01 Jan 1838':", 'Jan' in '01 Jan 1838')  # True
print ("'Feb' in '01 Jan 1838':", 'Feb' in '01 Jan 1838')  # False
