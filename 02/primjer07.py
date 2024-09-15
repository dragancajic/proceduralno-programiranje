'''
Napisati program koji ispisuje sve karaktere rečenice koja
se unosi sa tastature, sve do prve pojave karaktera 'a'.
Nakon prve pojave karaktera 'a' zaustaviti ispis.
'''

recenica = input("Unesite recenicu sa tastature: ")

for slovo in recenica:
    if slovo == 'a':
        print()  # predji u novi red, pa onda
        break
    else:
        print(slovo, end='_')
else:
    print()

# BOLJE JE BEZ (Pylint!), tj. može i bez else! <-- LOOK!
# Unnecessary "else" after "break", remove the "else" and de-indent
# the code inside itPylintR1723:no-else-break

for slovo in recenica:
    if slovo == 'a':
        print()  # predji u novi red, pa onda
        break
    print(slovo, end='_')
else:
    print()
