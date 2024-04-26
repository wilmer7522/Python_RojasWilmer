#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

with open("info.json", "r") as file:
    data=json.load(file)

ju=input()
nombre=input()
data[0]["estudiantes"].append({
"id": ju,
"nombre": nombre,
"apellido": "Rojas",
"edad": 40,
"fechaNacimiento": "10-05-1984",
"cedula": 1034310528,
"email": "wilmer7522@gmail.com",
"github": "https://github.com/wilmer7522/Python_RojasWilmer"
})


print(data[0]["estudiantes"][2])
eliminar = int(input("elimine"))
del data[0]["estudiantes"][eliminar]










with open("info.json" , "w") as file:
    json.dump(data,file)