usuario = []
saldo = []
suscripcion = []



def bienvenida():
    print("Bienvenido al periodico PyTimes")
    print("(1) agregar suscripcion\n(2) Comprar suscripcion a otro usuario\n(3) verificar suscripcion")
continuar = True
def menu():
    while continuar:
        bienvenida()
        elec = int(input())
        if elec == 1:
            nombre_usu = str(input(f"ingrese nombre {usuario}"))
            precio_Sus = 50
            print(f"Sr(a) {nombre_usu} el valor de su suscripcion anual es ${precio_Sus}")
            deseo = str.lower(input("desea susbribirse? si/no "))
            if deseo == "si":
                deposito = int(input(f"ingrese su deposito para poder comprar la suscripcion {saldo}" ))
                if deposito > precio_Sus:
                    deposito = deposito - precio_Sus
                    usuario.append(nombre_usu)
                    saldo.append(deposito)
                    print(f" su saldo disponible es {saldo}")
                else: 
                    print("saldo insuficiente debe ingresar mas saldo")
            else:
                print("Gracias por visitarnos")
            

menu()





    
    




