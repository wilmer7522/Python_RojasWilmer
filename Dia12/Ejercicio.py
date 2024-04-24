import json
#!/usr/bin/python
# -*- coding: utf-8 -*-
with open("large-file.json",encoding="utf-8") as openfile:
    miJson = json.load(openfile)
#print(miJson)
crearEventos=[]
for i in range(len(miJson)):
    if (miJson[i]["type"] == "CreateEvent"):
        crearEventos.append(miJson[i])
#print(crearEventos)
#print(miJson[0]["type"])

for q in range (5):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])

crearEventos[0]['type']="hola"
print(miJson[0]["type"])
for q in range (5):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",crearEventos[q]['id'])
    print("Tipo:",crearEventos[q]['type'])
    print("Actor:")
    print("------- ID:",crearEventos[q]['actor']['id'])
with open("eventos.json","w") as outfile:
    json.dump(crearEventos,outfile)
