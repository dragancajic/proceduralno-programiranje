#Od date liste brojeva kreirati novu listu u kojoj se nalaze kvadrati tih brojeva

brojevi = [1, 2, 3, 4, 5]

kvadrati = list(map(lambda x: x*x, brojevi))

print("Brojevi :", brojevi)
print("Kvdarati:", kvadrati)