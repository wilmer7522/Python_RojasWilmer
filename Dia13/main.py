#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import datetime
def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)


print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")
print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.Crear Estudiante\n4.Eliminar Estudiante\n")
x=int(input("Cual opción escoges:"))
miInfo=[]
if(x==1):
    miInfo=abrirArchivo()
    a=0
    for i in miInfo[0]["estudiantes"]:
        a = a +1
        print("################")
        print(" ESTUDIANTE #",a)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
elif(x==2):
    miInfo=abrirArchivo()
    contador = 0
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0
    estudiante = int(input("Cual Numero de estudiante vas a cambiar? "))
    datoCambiar=int(input("Que te gustaría cambiar del estudiante:\n1.Apellido:\n2.Nombre:\n3.Edad:\n4.Fecha de Nacimiento:\n5.Cedula:\n6.E-mail\n7.Github\n"))
    if (datoCambiar==1):
        nuevoApellido = input("Ingresa el nuevo apellido: ")
        miInfo[0]["estudiantes"][estudiante-1]["apellido"] = nuevoApellido
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    elif (datoCambiar==2):
        nuevoNombre = input("Ingresa el nuevo Nombre: ")
        miInfo[0]["estudiantes"][estudiante-1]["nombre"] = nuevoNombre
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    elif (datoCambiar==3):
        nuevaEdad = int(input("Ingresa la nueva edad: "))
        miInfo[0]["estudiantes"][estudiante-1]["edad"] = nuevaEdad
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    elif (datoCambiar==4):
        nuevaFechaNac = input("Ingresa la nueva Fecha de Nacimiento: ")
        fecha = datetime.datetime.strptime(nuevaFechaNac, "%d-%m-%Y")# Usamos datetime.datetime.strptime para convertir la cadena de fecha ingresada en un objeto de fecha con el formato especificado.
        fecha_format = fecha.strftime("%d-%m-%Y")# se uso el método strftime para formatear el objeto de fecha en una cadena con el formato DD-MM-AAAA.
        miInfo[0]["estudiantes"][estudiante-1]["fechaNacimiento"] = fecha_format
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    elif (datoCambiar==5):
        nuevaCedula = int(input("Ingresa la nueva Cedula: "))
        miInfo[0]["estudiantes"][estudiante-1]["cedula"] = nuevaCedula
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    elif (datoCambiar==6):
        nuevoEmail = input("Ingresa el nuevo E-mail: ")
        miInfo[0]["estudiantes"][estudiante-1]["email"] = nuevoEmail
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    elif (datoCambiar==7):
        nuevoGitHub = input("Ingresa el nuevo GitHub: ")
        miInfo[0]["estudiantes"][estudiante-1]["github"] = nuevoGitHub
        guardarArchivo(miInfo)
        print("Cambio realizado!")
        contador = 0
    miInfo=abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        contador = contador +1
        print("################")
        print(" ESTUDIANTE #",contador)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
    contador = 0

elif (x==3):
    miInfo=abrirArchivo()
    id_estu = int(input("Ingresa el ID del nuevo estudiante: "))
    for i in miInfo[0]["estudiantes"]:
        if id_estu == miInfo[0]["id"]:
            print("ID ya existe")
            break
        
        else:
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese Apellido: ")
            edad = int(input("Ingrese Edad: "))
            fechaNac = input("Ingrese fecha de Nacimiento (DD-MM-AAAA): ")
            cedula = int(input("Ingrese Numero de Cedula: "))
            email = input("Ingrese E-mail: ")
            github = input("Ingrese Github: ")
            miInfo[0]["estudiantes"].append({
            "id": id_estu,
            "nombre": nombre,
            "apellido": apellido,
            "edad": edad,
            "fechaNacimiento": fechaNac,
            "cedula": cedula,
            "email": email,
            "github": github
            })
            guardarArchivo(miInfo)
            print("Estudiante Creado con exito!!!")
            break
            
            
                
elif (x==4):
    a=0
    miInfo=abrirArchivo()
    
    for i in miInfo[0]["estudiantes"]:
        print("################")
        print("ESTUDIANTE #",a+1)
        print("ID:",i["id"])
        print("Nombre:",i["nombre"])
        print("Apellido:",i["apellido"])
        print("Edad",i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):",i["fechaNacimiento"])
        print("Cédula:",i["cedula"])
        print("E-mail:",i["email"])
        print("GitHub:",i["github"])
        print("################")
        print("")
        a = a + 1
    eliminar = int(input("Ingrese el ID del alumno a eliminar: "))

    del miInfo[0]["estudiantes"][eliminar]
    guardarArchivo(miInfo)
    print("eliminado con exito")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    


