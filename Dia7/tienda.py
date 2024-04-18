def tienda():
    print("Bienvenidos a la tienda virtual")
    print("(1) Agregar al carrito\n(2) Ver contenido del carrito\n(3) Calcular el total de la compra\n(4) Finalizar")
    muestra()    


productos = {"001":{"marca": "LG", "tipo": " Nevera", "precio": 1000000, "cantidad":10}, "002":{"marca": " Samsung", "tipo":" lavadora","precio": 900000 , "cantidad":12}}
preciosDic= {"001":1000000,"002":900000}
cantDic = {"001":10,"002":12}
def muestra():
    print("productos de la tienda")
    for id,i in productos.items():
        print(f"ID {id}\nMarca:{i["marca"]}\nTipo:{i["tipo"]}\nPrecio:{i["precio"]}\ncantidad: {i["cantidad"]}")
        print("")
tienda()
car ={}
compra ={}
totalFac = 0
var = True
seleccion = 0
#def carrito():
#    d = input("agregue id del producto ")
#    
#    if d in productos:
#        compra[d] = productos[d]
#        c = int(input("Ingrese cantidad "))
#        if c > 0:
#            compra[d]["cantidad"] = c
#            precio = preciosDic[d]
#            totalFac = totalFac + ((precio)*(c))
#        else:
#            print("la cantidad no puede ser negativa")
#    else:
#        print("producto no esta en el stock")





seleccion = input("Ingrese opcion ")
while var:
    
    if seleccion == "1":
        d = input("agregue id del producto ")
    
        if d in productos:
            compra[d] = productos[d]
            c = int(input("Ingrese cantidad "))
            if c > 0:
                compra[d]["cantidad"] = c
                precio = preciosDic[d]
                totalFac = totalFac + ((precio)*(c))
            else:
                print("la cantidad no puede ser negativa")
        else:
            print("producto no esta en el stock")   
    if seleccion == "2":
        print(totalFac)    

    
