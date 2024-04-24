n=input("")
lista = []
lista = list(sorted(set(map(int,n.split(",")))))
lista.sort()
target =  int(input())

cont=0

lista.append(target)
lista.sort()

for i in lista:
    cont+=1
    if target == i:
        print(cont-1)
        break   





        