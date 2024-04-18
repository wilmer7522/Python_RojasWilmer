usuario = []
usuario2 =[]
saldo = 0
deposito = 0
suscripcion = []
suscripcion2 = []
ti = 0


def bienvenida():
    print("Bienvenido al periodico PyTimes")
    print("(1) agregar suscripcion\n(2) Comprar suscripcion a otro usuario\n(3) verificar suscripcion\n(4) Recargar saldo\n(0) Salir del programa")
continuar = True
def menu():
    while continuar:
        bienvenida()
        elec = int(input())
        if elec == 1:
            
            nombre_usu = str(input(f"ingrese nombre "))
            precio_Sus = 50
            print(f"Sr(a) {nombre_usu} el valor de su suscripcion anual es ${precio_Sus}")
            deseo = str.lower(input("desea susbribirse? si/no "))
            if deseo == "si":
                deposito = int(input(f"ingrese su deposito para poder comprar la suscripcion " ))
                #saldo.append(deposito)
                if deposito > precio_Sus:
                    usuario.append(nombre_usu)
                    tiempo = int(input(f"Por cuanto tiempo en años desea comprar la suscripcion "))
                    suscripcion.append(tiempo)
                    deposito = deposito - (precio_Sus * tiempo)
                    #saldo.append(deposito)
                    print(f"ha comprado su suscripcion por {tiempo} año, su saldo disponible es {deposito}")
                else: 
                    print("saldo insuficiente debe ingresar mas saldo")
            else:
                print("Gracias por visitarnos")
        if elec == 2:
            if deposito < precio_Sus:
                print(f"saldo insuficiente debe recarcar\nSaldo: {deposito}")
            else:
                nom_usu2 = str(input("ingrese el nombre del usuario al que quiere comprar la suscripcion "))
                usuario2.append(nom_usu2)
                tiempo2 = int(input(f"Por cuanto tiempo en años desea comprar la suscripcion para {nom_usu2}"))
                suscripcion2.append(tiempo2)               
                deposito = deposito - (tiempo2 * precio_Sus)
                
            
            
            
                print(f"FELICIDADES!!!! has comprado una suscripcion para {nom_usu2} por {tiempo2} año, su saldo actual es {deposito}")
        if elec == 3:
            verificar = str(input(f"ingrese el nombre que desea verificar la suscrpcion "))
            if verificar in usuario:# or verificar in usuario2:
                print(f"El susario {usuario} tiene una suscripcion por {suscripcion} año")
            elif verificar in usuario2:
                print(f"El usario {usuario2} tiene una suscripcion por {suscripcion2} año")

        if elec == 4:
            print(f"Su saldo actual es ${deposito}")
            recarga = int(input(f"Cuanto desea recargar? "))
            deposito = deposito + recarga
            print(f"Su nuevo saldo es: ${deposito}")

        if elec == 0:
            print("gracias por visitarnos")
            break
        
            

            

menu()





    
    




