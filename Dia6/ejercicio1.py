

arreglo = []#arreglo vacio para guardar lo que el usuario ingrese
ent = list(set(map(int,input(arreglo).split()[0:300])))#el usuario ingresa la lista de numeros a verificar si estan duplicados y automaticamente los convierte en entero

part = True#se declara un boleano
while part == True:#while para condicionar el ciclo
    part = False#empezamos con False para que pase por el ciclo for
    for i in range(len(arreglo)-1):#ciclo for para pasar por todo el arreglo menos la ultima posicion 
        if arreglo[i] > arreglo[i+1]:#compara valores para ordenarlos
            acu = arreglo[i]#guarda el valor ordenado
            arreglo[i] = arreglo[i+1]#posiciona el valor ordenado a la siguiente casilla
            arreglo[i+1] = acu#y vuelve a guardar el valor en la nueva posicion
            part = True

print(ent)