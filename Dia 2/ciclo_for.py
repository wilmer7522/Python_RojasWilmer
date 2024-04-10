print("la sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1\n y continúa añadiendo números que son la suma de los dos anteriores")
print("\n por favor ingresa un numero hasta donde quiere que se detenga la sucesion de fibonacci")

n = input()
def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
    
fib(8)


for i in range():
    print(fib(i))


