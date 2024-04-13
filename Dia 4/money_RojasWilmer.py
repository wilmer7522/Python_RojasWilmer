
ingreso = int(input("Ingresa el dinero "))
lista = [10, 5,1]#se crea una lista para definir los valores 
suma = 0# se crea una variable para sumar la cantidad de monedas que se usaron para dar el cambio
cant = 0# se crea una variable para hacer el calculo de las monedas necesarias de cada tipo
for i in lista:
    if ingreso >=i:#se condiciona lo que ingresa el usuario con el incrementador mientras cumple la condicion
        cant= ingreso//i#se guarda el valor de la division de lo que ingresa el valor y lo que recorre i
        suma += cant
        print("la cantidad de monedas de",i, "son" ,cant)
        print("")
        ingreso= ingreso%i#se hace el calculo con el modulo de i en ese ciclo para it descartando los valores creados en lista

print("la suma de las monedas es: ",suma)

#Creado por camper Wilmer Rojas
 
