def buscar(nums, targ):#funcion para dos elementos a usar nums que son los que se sumaran y tatget ue seria el resultado a verificar
          
    for i in range(len(nums)):#se usa len para recorrer todos los elementos de la lista
        for j in range(i + 1, len(nums)):# for anidado se usa para verificar el i+1 para empezar desde la posicion 1 para no repetir elementos de la lista
            if nums[i] + nums[j] == targ:#suma los dos elementos de la lista par saber si da el resultado ingresado en el target
                arr.append((i,j))#si se cumple agrega los elementos a la lista vacia
    return arr
arr = []#lista vacia
num = input().split()#ingresa los numeros
num = [int(n)for n in num]#convierte a enteros
targ = int(input())#ingresa el numero del resultado
mostrar = buscar(num,targ)#se usa nueva variable para llamar la funcion con la lista agregada por el usuario

for a in mostrar: #se ordena la variable para luego mostrarla
    print(a)


















