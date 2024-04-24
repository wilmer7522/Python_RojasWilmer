miJSON= {
  "response": "success",
  "id": "1",
  "name": "A-Bomb",
  "powerstats": {
    "intelligence": "38",
    "strength": "100",
    "speed": "17",
    "durability": "80",
    "power": "24",
    "combat": "64"
  },
  "biography": {
    "full-name": "Richard Milhouse Jones",
    "alter-egos": "No alter egos found.",
    "aliases": [
      "Rick Jones"
    ],
    "place-of-birth": "Scarsdale, Arizona",
    "first-appearance": "Hulk Vol 2 #2 (April, 2008) (as A-Bomb)",
    "publisher": "Marvel Comics",
    "alignment": "good"
  },
  "appearance": {
    "gender": "Male",
    "race": "Human",
    "height": [
      "6'8",
      "203 cm"
    ],
    "weight": [
      "980 lb",
      "441 kg"
    ],
    "eye-color": "Yellow",
    "hair-color": "No Hair"
  },
  "work": {
    "occupation": "Musician, adventurer, author; formerly talk show host",
    "base": "-"
  },
  "connections": {
    "group-affiliation": "Hulk Family; Excelsior (sponsor), Avengers (honorary member); formerly partner of the Hulk, Captain America and Captain Marvel; Teen Brigade; ally of Rom",
    "relatives": "Marlo Chandler-Jones (wife); Polly (aunt); Mrs. Chandler (mother-in-law); Keith Chandler, Ray Chandler, three unidentified others (brothers-in-law); unidentified father (deceased); Jackie Shorr (alleged mother; unconfirmed)"
  },
  "image":[{"id":"1","url":"google.com"},{"id":"2","url":"facebook.com"}]}

#print(type(miJSON))

#miJSON['image'] = {
 #   "pepito": "https://www.superherodb.com/pictures2/portraits/10/100/10060.jpg"
 # }
#del miJSON['image']['url2']
#print(miJSON['image'][1]["url"])
#miJSON.update({'grupazo':'T2'})
#print(miJSON)


#variable = miJSON['image']
#del miJSON['image']
#miJSON.update({'imagenes':variable})
#print(miJSON)

x=input("Ingresa el valor que quieres consultar: 1:Apariencia, 2:Trabajos, 3:Imágenes:")
if (x=="1"):
    print("")
    print("##############################")
    print("####APARIENCIAS####")
    print("##############################")
    print(type(miJSON["appearance"]))
    for a,b in miJSON["appearance"].items():
        print(a,b)
elif(x=='2'):
    print("")
    print("##############################")
    print("####TRABAJOS####")
    print("##############################")
    print(type(miJSON["work"]))
    for a,b in miJSON["work"].items():
        print(a,b)
elif(x=='3'):
    print("")
    print("##############################")
    print("####IMÁGENES####")
    print("##############################")
    print(type(miJSON["image"]))
    for a in miJSON["image"]:
        print(a)