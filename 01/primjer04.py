'''
                        ---Konverzija brojeva iz jednog tipa u drugi---
'''

X = 1    # int
Y = 2.8  # float
Z = 1j   # complex

# Konverzija - int u float:
a = float(X)
print("a =", a)

# Konverzija - int u complex:
b = complex(X)
print("b =", b)

# Konverzija - float u int:
C = int(Y)
print("C =", C)

# Konverzija - float u complex:
d = complex(Y)
print("d =", d)

# Konverzija - complex u int - nije dozvoljeno!
#e = int(Z)

# Konverzija - complex u float - nije dozvoljeno!
#f = float(Z)

print("type(a):", type(a))
print("type(b):", type(b))
print("type(C):", type(C))
print("type(d):", type(d))
