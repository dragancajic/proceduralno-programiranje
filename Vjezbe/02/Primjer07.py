# Napisati program koji ispisuje sve karaktere rečenice
# koja se unosi sa tastature, sve do prve pojave karaktera 'a'.
# Nakon prve pojave karaktera 'a' zaustaviti ispis.

recenica = input("Unesite recenicu sa tastature: ")

for slovo in recenica:
    if (slovo == 'a'):
        break
    else:
        print(slovo)

# može i bez else!

# for slovo in recenica:
#     if(slovo == 'a'):
#         break
#     print(slovo)
