'''
Napisati program koji ispisuje broj koji se dobije izbacivanjem cifre desetica
iz unesenog pozitivnog broja.
'''

broj = int(input("Unesite pozitivan broj: "))
print("Uneseni broj je:", broj)

jedinice = broj % 10
broj //= 100      # broj = broj // 100
broj *= 10        # broj = broj * 10
broj += jedinice  # broj = broj + jedinice

print("Broj nakon izbacivanja cifre desetica:", broj)
