
ingreso = int(input("Ingresa el dinero "))
lista = [10, 5,1]
suma=0
for i in lista:
    if ingreso >=i:
        cant= ingreso//i
        suma= cant+cant
        print("la cantidad de monedas de",i, "son" ,cant)
        print("")
        ingreso= ingreso%i

print("la suma de las monedas es: ",suma)
 
