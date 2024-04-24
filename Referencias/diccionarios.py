dici = {"nombre": "wilmer","edad": "39","telefono": "123456789" }
while 1:
    print(dici)
    nuevo = input("datos son: " + dici["nombre"]+ " " + "edad " + dici["edad"] + " ")
    valor = input("ingrese nuevo valor ")
    print("")
    print(dici)
    dici[nuevo] = valor
    eleccion = int(input("(1) Si (0) No"))
    if eleccion == 1:
        print("salir")
        break