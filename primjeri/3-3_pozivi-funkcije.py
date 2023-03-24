#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 00:54:02 2023

@author: dragancajic
"""

def func(name, surname = 'Cajic', **nicknames):
    print(name, surname, nicknames)


lista = ["Bojan", "Dragan"]
rjecnik = {"name": "Dragan", "surname": "Cajic"}
nadimci = ("Gagi", "Gaga", "Dragisa")
zanimanja = ("profesor", "doktor", "naucnik")
naucnici = {"theory": "Relativity", "practice": "Nuclear"}

# primjeri poziva funkcije / odgovarajuci oblici argumenata
func("vrijednost1", 2)
func(surname = "Lukijanovic", name = "Dragan")

print("-" * 20)  # razdvajanje ispisa

func(*lista)
func(**rjecnik)

print("-" * 20)  # razdvajanje ispisa

func("Zlatan", "Stipi$ic")  # poziciona vrijednost argumenata
func(name = "Nikola", surname = "Tesla")  # imenovani argumenti
func("Nada")  # podrazumjevana vrijednost prezimena se koristi!

print("-" * 20)  # razdvajanje ispisa

#func("Mihajlo", "Pupin", *zanimanja)
func("Albert", "Ajn$tajn", **naucnici)

# def func(*other, name)
# def func(*, name=value)
