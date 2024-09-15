#Transformisati listu imena tako da prvo slovo imena bude veliko, a ostala mala

imenaMalaSlova = ["marko", "ana", "sara", "milos", "sanja"]

velikoPocetnoSlovo = lambda rijec: rijec[:1].upper() + rijec[1:]

imenaVelikoPocetnoSlovo = list(map(velikoPocetnoSlovo, imenaMalaSlova))

print(imenaVelikoPocetnoSlovo)