# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 02:16:05 2026

@author: diogo
"""

import csv 

with open("utilizadores.csv", "w", newline="", encoding="utf-8-sig") as ficheiro: 
    escritor = csv.DictWriter(ficheiro, fieldnames=["nome", "email"], delimiter=";") 
    escritor.writeheader() 
    
    for pessoa in utilizadores: 
        escritor.writerow({"nome": pessoa["name"], "email": pessoa["email"]}) 

print("CSV de utilizadores criado")