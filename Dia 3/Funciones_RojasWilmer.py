
input("Bienvenido al Programa \n(ENTER PARA CONTINUAR)")
print("")
input("Este es un programa para verificar si un numero es primo o no es primo: \n(ENTER PARA CONTINUAR)")
print("")
def lista_menu():
        print("¿Que deseas hacer?\n(1) Verificar Numero\n(2) Salir del Programa\n(3) Información Adicional")
continuar = True
def menu():
    while continuar:
    
        lista_menu()
        opcion = int(input())
        if opcion == 1:
        
            def np(n):
                return n
            n = int(input("ingrese un numero "))
            print("")
            numero = np(n) 
            if numero == 1:
                print(numero,"no es primo")
                print("")
            elif numero == 3 or numero == 2:
                print(numero,"es primo")
                print("")
            elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 11 == 0:
                print(numero,"no es primo")
                print("")
            else:
                print(numero,"es primo")
                print("")
        elif opcion == 2:
                print("Has salido del programa")
                break
        elif opcion == 3:
                print("""En matemáticas, un número primo es un número natural mayor que 1\n que tiene únicamente dos divisores positivos distintos: él mismo y el 1. \nPor contrario, los números compuestos son los números naturales\nque tienen algún divisor natural\naparte de sí mismos y del 1,\ny, por lo tanto, pueden factorizarse.""")
                print("")
                print("Realizado por el Camper Wilmer Rojas")
                print("")
if __name__ == '__main__':
    menu()   

print("BIENVENIDO AL GENERADOR DE CONTRASEÑAS")
input("ENTER PARA CONTINUAR")
print("")
print("Este programa genera contraseñas de manera aleatoria a solicitud del usuario\npuedes escoger entre mayusculas, minusculas, numeros y simbolos para generar tu contraseña segura")
input("ENTER PARA INICIAR")
print("")
def lista():
        print("Elige la longitud de tu comtraseña entre 8 y 15 caractares")
        print("(1) ¿Quieres que tenga mayusculas?")
        print("(2) ¿Quieres que tenga minusculas?")
        print("(3) ¿Quieres que tenga numeros?")
        print("(4) ¿Quieres que tenga simbolos?")
        print("(5) Salir")
seguir = True
def men():
    while seguir:
        lista()
        pa = int(input())
        if pa == 1:
             
            import random, string

            def contra(n):
                todo1 = list(string.ascii_uppercase)+list(string.ascii_letters)
                
                p = []
                                                
                for i in range(n):
                    nw = random.choice(todo1)
                    p.append(nw)
                final = "".join(p)
                return final
            n = int(input("teclea la longitud de tu contraseña "))
            salida = contra(n)
            print(salida)
            print("")
            
        elif pa == 2:
            import random, string
            def contra(n):
                
                todo2 = list(string.ascii_lowercase)
                                
                p2 = []
                for i in range(n):
                    nw = random.choice(todo2)
                    p2.append(nw)
                final = "".join(p2)
                return final
            n = int(input("teclea la longitud de tu contraseña "))
            salida = contra(n)
            print(salida)
            print("")
        elif pa == 3:
            import random, string
            def contra(n):
                todo3 = list(string.digits)
                p3 = []
                for i in range(n):
                    nw = random.choice(todo3)
                    p3.append(nw)
                final = "".join(p3)
                return final
            n = int(input("teclea la longitus de tu contraseña "))
            salida = contra(n)
            print(salida)
            print("") 
  
        elif pa == 4:
            import random, string
            def contra(n):
                todo = list(string.punctuation)
                p4 = []
                for i in range(n):
                    nw = random.choice(todo)
                    p4.append(nw)
                final = "".join(p4)
                return final
            n = int(input("teclea la longitud de tu contraseña "))
            salida = contra(n)
            print(salida)
            print("")
            input("ENTER PARA CONTINUAR")
            print("")     
        
        elif pa == 5:
            print("Haz salido del programa")
            input("Presione ENTER para finalizar")
            break

        elif pa != 1 or pa != 2 or pa != 3 or pa != 4 or pa != 5:

            print("opcion invalida")
            print("")
            input("precione ENTER para continuar")
            print("")
        
        
        
        
        
        
            



if __name__ == '__main__':
    men()   

