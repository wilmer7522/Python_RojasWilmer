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
  "image": {
    "url": "https://www.superherodb.com/pictures2/portraits/10/100/10060.jpg"
  }
}

print(type(miJSON))
print(miJSON["image"]["url"])
miJSON ["image"] = {
    "pepito": "https://www.superherodb.com/pictures2/portraits/10/100/10060.jpg"}

#del miJSON ["image"]#eliminar
print(miJSON["image"])
miJSON.update({"grupo":"T2"})#agregar 
variable = miJSON["image"]#agrega lo que esta en image en una variable
del miJSON["image"]#borra el nombre image
miJSON.update({"imagenes":variable})#actualiza el nombre por imagenes

print(miJSON)
x = input("ingresa 1: ")
if (x=="1"):
    print("")
    print(type(miJSON["appearance"]))
    for a,b in miJSON["appearance"].items():
        print(a,b)

