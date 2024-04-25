import json
#!/usr/bin/python
# -*- coding: utf-8 -*-
with open("large-file.json",encoding="utf-8") as openfile:
    datos = json.load(openfile)
#print(datos)
PublicEvent=[]
for i in range(len(datos)):
    if (datos[i]["type"] == "PublicEvent"):
        PublicEvent.append(datos[i])
#print(PublicEvent)
#print(datos[0]["type"])

for q in range (len(PublicEvent)):
    print("#######################")
    print("#### Evento # ",q+1 ,"##")
    print("#######################")
    print("ID: ",PublicEvent[q]['id'])
    print("Tipo:",PublicEvent[q]['type'])
    print("Actor:")
    print("--------ID:",PublicEvent[q]['actor']['id'])
    print("--------login:",PublicEvent[q]["actor"]["login"])
    print("--------Gravatar ID:",PublicEvent[q]["actor"]["gravatar_id"])
    print("--------url:",PublicEvent[q]["actor"]["url"])
    print("--------avatar_url:",PublicEvent[q]["actor"]["avatar_url"])
    print("Repo:")
    print("--------ID:",PublicEvent[q]['repo']['id'])
    print("--------name:",PublicEvent[q]['repo']['name'])
    print("--------url:",PublicEvent[q]['repo']['url'])
    print("--------Public:",PublicEvent[q]['public'])
    print("--------created_at:",PublicEvent[q]['created_at'])


    

#PublicEvent[0]['type']="hola"
#print(datos[0]["type"])
#for q in range (5):
#    print("#######################")
#    print("#### Evento # ",q+1 ,"##")
#    print("#######################")
#    print("ID: ",PublicEvent[q]['id'])
#    print("Tipo:",PublicEvent[q]['type'])
#    print("Actor:")
#    print("------- ID:",PublicEvent[q]['actor']['id'])
with open("eventos.json","w") as outfile:
    json.dump(PublicEvent,outfile)
