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

for i in range (1,5):
    print(i)


while True:
    print("ingrese la palabra clave")
    entrada = input()

    if entrada == "buenos dias":
        print("es hora de levantarse")
        break
    else:
        print("no ingreso la palabra clave")


#Funciones (4 Tipos)
#sin parametros sin retorno
def python():
    print("esto es python!!!") 
python()

#sin parametros con retorno
def retorno():
    return 50
numero = retorno()
print("el numero retornado es ", numero)

#con parametros sin retorno
def bienvenido(nombre):
    print("bienvenido a python", nombre)
    
nombre_ingresado = input("Ingresa tu nombre ")
bienvenido(nombre_ingresado)

#con parametros con retorno
def con_parametro(a,b):
    return a+b
a = "hola "
b = "bienvenido a python"
mensaje = con_parametro(a,b)
print(mensaje)


#Desarrollado por Wilmer Rojas - C.C 134310528