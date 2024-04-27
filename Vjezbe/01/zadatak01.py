'''
Napisati program koji sa tastature učitava četvorocifren broj i na ekran
ispisuje zbir cifara tog broja.
'''

broj = int(input("Unesite cetvorocifren broj: "))

jedinice = broj % 10
desetice = (broj // 10) % 10
stotine = (broj // 100) % 10
hiljade = broj // 1000

zbirCifara = jedinice + desetice + stotine + hiljade
print(f"Zbir cifara unesenog broja {broj} je {zbirCifara}.")
