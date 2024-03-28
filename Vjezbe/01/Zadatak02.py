'''
Napisati program koji sa tastature učitava dužinu stranice jednakostraničnog
trougla, a na ekran ispisuje površinu jednakostraničnog trougla.
'''

import math

stranica = float(input("Unesite duzinu stranice jednakostranicnog trougla: "))

#povrsina = (stranica**2 * math.sqrt(3)) / 4
povrsina = (math.pow(stranica, 2) * math.sqrt(3)) / 4

print(f"Povrsina jednakostranicnog trougla stranice {stranica} je {povrsina:.3f}.")
