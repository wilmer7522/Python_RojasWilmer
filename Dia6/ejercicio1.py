def ordenar(arr):
    n = len(arr)
arreglo = []

ent = list(set(input(arreglo).split()))
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

    print(ent)