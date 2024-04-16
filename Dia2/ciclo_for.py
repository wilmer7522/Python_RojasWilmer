    


while True:
    print("la sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1\n y continúa añadiendo números que son la suma de los dos anteriores")

    print("\nPor favor ingresa un número hasta donde quieres que se detenga la sucesión de Fibonacci (ingresa '0' para salir):")
    numero = input()
    numero = int(numero)
    
    A = 0
    B = 1

    for i in range(1, numero):
        while B < 89:
            print(B)
            break
        C = B
        B = C + A
        A = C
    
    print("¿Desea continuar? (1)si (2)no:")
    respuesta = int(input())
    if respuesta == 2:
        print("Saliendo del programa...")
        break
    elif respuesta == 1:
        print("sigamos")
















