dici = {"nombre": "wilmer","edad": "39","telefono": "123456789" }
while 1:
    print(dici)
    nuevo = input("datos son: " + dici["nombre"]+ " " + "edad " + dici["edad"] + " ")
    valor = input("ingrese nuevo valor ")
    dici[nuevo] = valor