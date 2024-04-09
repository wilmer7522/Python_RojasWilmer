#--------------------------
#----DIA 1 SHEET PYTHON----
#--------------------------

#IMPRIMIR HOLA MUNDO

print("Hola mundo")


#Datos primitivos
#numero
numero = 10 #nombrevariable = valorvariable
print(numero) # imprimir variable
print(type(numero)) # imprime tipo de variable

#flotante
numerodecimal = 20.5
print(numerodecimal)
print(type(numerodecimal))

#boleano
boleano = True
print(boleano)
print(type(boleano))

#cadena de texto
texto = "hola Mundo"
print(texto)
print(type(texto))

#Ingresa por teclado la infomarcion
print("ingresa tu nombre")
nuevo = input() 
print("Tu nombre es", nuevo)

#Conversion de tipos de variable
numerico = 10
print(type(numerico))
numerico = float(numerico)
print(type(numerico))
numerico = bool(numerico)
print(type(numerico))
numerico = str(numerico)
print(type(numerico))

#Bucles For y While
num = [2,4,6,8]
for i in num:
    print(i)

#Funciones (4 Tipos)

#Desarrollado por Wilmer Rojas - C.C 134310528