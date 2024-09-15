#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:03:01 2024

@author: dragancajic
"""

# Folder u kojem se nalazi datoteka

import os
print(os.getcwd())  # cwd - Current Working Directory √
# /home/dragancajic/Devs/pmfbl/pp/vjezbe-06/obrada-datoteka

#os.chdir('C:\\Users\\Milica\\Desktop\\UOAR2 i UR2\\Vježbe\\Vježbe 4')
os.chdir('..')      # chdir - CHange DIRectory  √
print(os.getcwd())  # '/home/dragancajic/Devs/pmfbl/pp/vjezbe-06'
