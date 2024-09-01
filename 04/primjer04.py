'''
                    ---Iteracija kroz listu---
'''

L = [1, 2, 3,14, True, False, 5.12, "abc", "xyz"]

# prvi način
for i in range(len(L)):
    print(L[i], end=" ")
print()

# drugi način
i = 0
while i < len(L):
    print(L[i], end=" ")
    i += 1
print()

# treci način
for element in L:
    print(element, end=" ")
print()
