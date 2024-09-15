#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:08:36 2024

@author: dragancajic
"""

# ~ Raw stringovi ~

# -----------------------
# ~ енгл. `raw strings` ~
# -----------------------
# што би у српском језику ["Причај српски, да те читав свет разуме! ;-)"] било:

# • "сирове"/ИЗВОРНЕ ниске [низови симбола/карактера],
# • "чисте" ниске / "чисти" низови симбола
# (без ПОСЕБНОГ ЗНАЧЕЊА одређених карактера - енгл. special/`escape characters`),
# • основни низови симбола, `изворни низови симбола, без додатног значења!`. √

# Stringovi mogu sadržavati specijalne karaktere kao što su \n, \t, \\, \", ...

# Raw stringovi tretiraju ovakve karaktere kao bilo koji drugi karakter
# (nemaju specijalno značenje)!

# Npr.
STRING = "Fića\tTea\nJela"
print(STRING)

# output:
# Fića    Tea
# Jela


raw_string = r"Fića\tTea\nSaša"
print(raw_string)

# output:
# Fića\tTea\nSaša
