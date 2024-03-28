#                           ---Konverzija brojeva iz jednog tipa u drugi---

x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Konverzija - int u float:
a = float(x)
print("a =", a)

# Konverzija - int u complex:
b = complex(x)
print("b =", b)

# Konverzija - float u int:
c = int(y)
print("c =", c)

# Konverzija - float u complex:
d = complex(y)
print("d =", d)

# Konverzija - complex u int - nije dozvoljeno!
#e = int(z)

# Konverzija - complex u float - nije dozvoljeno!
#f = float(z)

print("type(a):", type(a))
print("type(b):", type(b))
print("type(c):", type(c))
print("type(d):", type(d))
