# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 02:14:53 2026

@author: diogo
"""


import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    utilizadores = resposta.json()

    print("Total de utilizadores:", len(utilizadores))

    for pessoa in utilizadores:
        print(pessoa["name"], "-", pessoa["email"])

    pesquisa = input("Introduza o nome do utilizador que pretende pesquisar: ")

    encontrados = 0

    for pessoa in utilizadores:
        if pesquisa in pessoa["name"]:
            print(pessoa["name"], "-", pessoa["email"])
            encontrados += 1

    if encontrados == 0:
        print("Não foram encontrados utilizadores com esse nome.")

    import csv

    with open("utilizadores.csv", "w", newline="", encoding="utf-8-sig") as ficheiro:
        escritor = csv.DictWriter(ficheiro, fieldnames=["nome", "email"], delimiter=";")
        escritor.writeheader()

        for pessoa in utilizadores:
            escritor.writerow({"nome": pessoa["name"], "email": pessoa["email"]})

    print("CSV de utilizadores criado")

except requests.exceptions.RequestException as erro:
    print("Não foi possível consultar a API:", erro)


