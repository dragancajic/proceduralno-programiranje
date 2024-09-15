'''
~ Primjer 6 ~

`with open(file) as name_of_file` <-- LOOK! није потребно `close()`!
'''

with open("ulaz.txt", "r", encoding='utf-8') as inputFile:
    for line in inputFile:
        print(line, end="")

# kada koristimo rezervisanu riječ `with` datoteka će se automatski
# zatvoriti -- nije potrebno da je mi eksplicitno zatvorimo! :eyes:
