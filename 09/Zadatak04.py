#Napisati rekurzivnu funkciju koja racuna NZD dva prirodna broja.

def NZD(a, b):
    manji = min(a, b)
    veci = max(a, b)

    if manji == 0:
        return veci
    
    if manji == 1:
        return 1
    
    return NZD(manji, veci % manji)

a = int(input("Unesite prirodan broj a:"))
b = int(input("Unesite prirodan broj b:"))

print(f"NZD({a},{b}) = {NZD(a, b)}")