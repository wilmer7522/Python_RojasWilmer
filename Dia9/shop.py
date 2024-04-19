car = []#lista vacia
can = int(input(f"ingrese la cantidad de articulos que quieres ingresal al carrito "))#ingrea la cantidad de articulos
nombreProductos = []#independiza el nombre que esta en car
precioProductos = []#independiza el precio que esta en car
cantidadProductos= []#independiza la cantidad que esta en car
menu = True
while menu:
    for i in range(can):
         
            nombre = str(input("ingrese nombre del articulo "))
            print("")
            precio = int(input(f"ingrese precio el precio de {nombre} "))
            print("")
            cantidad = int(input(f"ingrese la cantidad de {nombre} a agregar al carrito "))
            nombreProductos.append(nombre)#agregar nombre a la lista nombreProductos
            precioProductos.append(precio)#agregar precio a la lista precioPriductos
            cantidadProductos.append(cantidad)#agregar cantidad a la lista cantidadProductos


        

    for i in range(can):
        print(f"descripcion articulo: ARTUCULO {nombreProductos[i]} PRECIO: ${precioProductos[i]} CANTIDAD: {cantidadProductos[i]}")#imprime la lista de los articulos agregados
    
        
    break                              
                                  
