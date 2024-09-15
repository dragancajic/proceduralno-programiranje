#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 10:08:58 2024

@author: dragancajic
"""

# ~ Specijalni karakteri i sekvence ~

# Specijalni karakteri su:  \ . ? * + ^ $ | ( ) [ ] { }
# Specijalne sekvence su: \d \D \w \W \s \S \A \Z \B \b


# • Predstavljanje skupova •

# » KREIRANJE SKUPA karaktera:
# Za kreiranje se koriste specijalni karakteri `[ ]` unutar kojih se navode
# elementi skupa.

#----------|------|
# Primjeri - Opis |
#----------|-----~|
# [abc]    - Karakteri se mogu NABRAJATI POJEDINAČNO, a navode se jedan za
#            drugim bez razmaka.
# [a-c]    - Može se ZADATI OPSEG karaktera korišćenjem znaka `–`.
# [^abc]   - Mogu se izabrati samo KARAKTERI koji se nalaze VAN SKUPA
#            korišćenjem znaka `^` na početku skupa.
# [.?*+(}] - Specijalni karakteri NEMAJU specijalno ZNAČENJE UNUTAR skupa!


# » Korišćenje postojećih skupova √

# .  - Bilo koji karakter sem novog reda
# \d - Bilo koja decimalna cifra [0-9]
# \D - Sve što nije decimalna cifra [^0-9]
# \w - Bilo koji word karakter [a-zA-Z0-9_]
# \W - Sve što nije word karakter [^a-zA-Z0-9_]
# \s - Bilo koji whitespace karakter [ \t\n\r\f\v]
# \S - Sve što nije whitespace karakter [^ \t\n\r\f\v]

# ~ Napomena:
# \. - Sama tačka, ne znači bilo koji karakter (analogno za ostale specijalne karaktere)
