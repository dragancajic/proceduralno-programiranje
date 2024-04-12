# Napisati program koji ispisuje sve karaktere rečenice
# koja se unosi sa tastature, osim karaktera 'a'.

recenica = input("Unesite recenicu sa tastature: ")

for slovo in recenica:
    if(slovo == 'a'):
        continue
    else:
        print(slovo, end = " ")
