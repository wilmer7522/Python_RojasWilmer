import random #declaracion para generar numero aleatorios


numero_secreto = random.randint(1, 100) # Genera un número aleatorio entre 1 y 100 randint es para numeros enteros y uniform para numeros flotantes
while True:
    
    print("ingresa un numero entre 1 y 100 para adivinar el numero secreto")
    numero = int(input())
    if numero == numero_secreto:
        print("FELICIDADES!!! adivinaste el numero secreto")
        break
    elif numero < numero_secreto:
        print("el numero secreto es mayor que el ingresado")
    elif numero > numero_secreto:
        print("el numero secreto es menor que el ingresado")



























































































































































































































