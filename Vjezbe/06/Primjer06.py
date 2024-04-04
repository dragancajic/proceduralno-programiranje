with open("ulaz.txt", "r") as inputFile:
    for line in inputFile:
        print(line, end="")

# kada koristimo rezervisanu riječ `with` datoteka će se automatski
# zatvoriti -- nije potrebno da je mi eksplicitno zatvorimo! :eyes:
