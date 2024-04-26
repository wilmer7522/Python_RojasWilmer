#!/usr/bin/python
# -- coding: utf-8 --
import json

def abrirArchivo():
    miJSON=[]
    with open('info.json','r') as openfile:
        miJSON= json.load(openfile)
    return miJSON

def guardarArchivo(miData):
    with open("info.json","w") as outfile:
        json.dump(miData,outfile)

def crearEvento(miInfo):
    nuevo_evento = {}
    nuevo_evento["nombre"] = input("Ingrese el nombre del evento: ")
    nuevo_evento["fecha"] = input("Ingrese la fecha del evento (DD-MM-AAAA): ")
    nuevo_evento["descripcion"] = input("Ingrese la descripción del evento: ")
    # Agregar el nuevo evento a la lista de eventos
    miInfo[0]["eventos"].append(nuevo_evento)
    guardarArchivo(miInfo)
    print("Evento creado exitosamente.")

def eliminarEvento(miInfo):
    print("Eventos disponibles para eliminar:")
    for index, evento in enumerate(miInfo[0]["eventos"], start=1):
        print(f"{index}. {evento['nombre']} - {evento['fecha']}")
    opcion = int(input("Seleccione el número del evento que desea eliminar: "))
    del miInfo[0]["eventos"][opcion - 1]
    guardarArchivo(miInfo)
    print("Evento eliminado exitosamente.")

def actualizarEvento(miInfo):
    print("Eventos disponibles para actualizar:")
    for index, evento in enumerate(miInfo[0]["eventos"], start=1):
        print(f"{index}. {evento['nombre']} - {evento['fecha']}")
    opcion = int(input("Seleccione el número del evento que desea actualizar: "))
    campo = input("Seleccione el campo que desea actualizar (nombre, fecha, descripcion): ")
    nuevo_valor = input("Ingrese el nuevo valor: ")
    miInfo[0]["eventos"][opcion - 1][campo] = nuevo_valor
    guardarArchivo(miInfo)
    print("Evento actualizado exitosamente.")

def revisarEventos(miInfo):
    print("Lista de eventos:")
    for index, evento in enumerate(miInfo[0]["eventos"], start=1):
        print(f"{index}. Nombre: {evento['nombre']}, Fecha: {evento['fecha']}, Descripción: {evento['descripcion']}")

print("################")
print("## PLATAFORMA DE GESTION ##")
print("################")
print("")
print("Hola! Por favor escoge alguna de las opciones:\n1.Revisar estudiantes\n2.Modificar estudiante\n3.Eliminar estudiantes\n4.Actualizar estudiantes")
x = int(input("Cual opción escoges: "))
miInfo = []

if x == 1:
    miInfo = abrirArchivo()
    for i in miInfo[0]["estudiantes"]:
        print("################")
        print("ID:", i["id"])
        print("Nombre:", i["nombre"])
        print("Apellido:", i["apellido"])
        print("Edad", i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):", i["fechaNacimiento"])
        print("Cédula:", i["cedula"])
        print("E-mail:", i["email"])
        print("GitHub:", i["github"])
        print("################")
        print("")
elif x == 2:
    miInfo = abrirArchivo()
    contador = 0
    for i in miInfo[0]["estudiantes"]:
        contador = contador + 1
        print("################")
        print(" ESTUDIANTE #", contador)
        print("ID:", i["id"])
        print("Nombre:", i["nombre"])
        print("Apellido:", i["apellido"])
        print("Edad", i["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):", i["fechaNacimiento"])
        print("Cédula:", i["cedula"])
        print("E-mail:", i["email"])
        print("GitHub:", i["github"])
        print("################")
        print("")

elif x == 3:
    miInfo = abrirArchivo()
    eliminarEvento(miInfo)

elif x == 4:
    miInfo = abrirArchivo()
    actualizarEvento(miInfo)