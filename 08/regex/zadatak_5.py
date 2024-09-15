#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 07:37:50 2024

@author: dragancajic
"""

# Zadatak 5 - Domaći

# Na programskom jeziku Python sastaviti program koji izdvaja različite riječi
# iz HTML datoteke. Ignorisati sadržaj zadat između oznaka `<>`.
"""
Primjer HTML datoteke:

<html>
    <head>
        <title>Jednostavan HTML dokument</title>
    </head>
    <body>
        <p> Prvi paragraf.</p>
        <p>Drugi paragraf!</p>
    </body>
</html>
"""

import re

with open("html.txt") as html:
    content = html.read()

pattern = re.compile(r"<[^<>]+>|[\s,.!?]+")
words = pattern.split(content)
words = set(words)
words.remove("")

print(*words, sep=" ")
