import json

lista = "large-file.json"


with open(lista,encoding="utf-8") as file:#abre o llama el archivo .json y codifica en formato utf-8 
    datos = json.load(file)#crea nueva vaiable para cargar con load()
    
      
    
    
volver = True
while volver:    
    print("==========================================================")    
    print("ingrese el numero de la opcion que desea, entre(1-4)")
    print("==========================================================")
    print("")
    print("")
    print("(1) Crear\n(2) Leer\n(3) Actualizar\n(4) Eliminar\n(0) Salir")
    


    
        
        
    opt = int(input())
    if opt == 1:
        
        id_crear = (input("Ingrese ID: "))#ingresamos el id que se va a crear "id"
        crear = input("ingrese nuevo evento: ")#ingresamos el nombre del evento que se guarda en "type"
        nuevo = {"type": crear, "id": id_crear}#se guardan ambos datos en un diccionario
        datos.append(nuevo)#se pasan los datos del diccionario a datos
        
        
        print(f"Nuevo evento llamado {[crear]} agregado")
        


    elif opt == 2:
        if datos:
            #tipo = input("ingrese tipo de evento")
            for i, evento in enumerate(datos,1):#recorre i en toda la lista enumerando cada valor 
            #    evento.append(tipo)
            #print(datos[0]["type"])            
                print(f"numero:{i+1} - ID:{evento["id"]} - Type:{evento["type"]} - Actor:{evento["actor"]} - Repo:{evento["repo"]}")#imprime lista com su respectivo ID
            #print("")
                

    
    elif opt == 3:
        id_act = input("Ingrese el ID del evento que desea actualizar: ")#se pide ingresar el numero de id para buscar y actualizar
        for evento in datos:#recorre evento en los datos que son los que estan todos los diccionarios
            if evento["id"] == id_act: #verifica si el id ingresado esta dentro de el id de evento
                n_tip = input("Ingrese el nuevo tipo de evento: ") #pide ingresar el nuvo nombre del evento de "type"
                evento["type"] = n_tip#pasa lo que se ingreso anteriormente a evento en la clave "type"
                print("Evento actualizado")
                print("")
                break
        else:
            print("ID no encontrado")
            print("")
            break
        
    elif opt == 4:
        borrar_id = input("Ingrese el id que desea borrar: ")#pide el id que se desea borrar asociado al evento ("type")
        for evento in datos:#recorre evento en los datos que son los que estan todos los diccionarios
            if evento["id"] == borrar_id:#verifica si el id ingresado esta dentro de el id de evento
                datos.remove(evento) #elimina los datos asociados al id que estan en datos          
            
                print("evento eliminado")
                print("")
                break
        else:   
            print("ID no existe")
            print("")
            break

    elif opt == 0:
        print("Terminando el programa...")
        volver = False

with open("eventos.json","w") as outfile:
    json.dump(datos,outfile)
    
    
    
    
    
    
    
    
    
    



  
    
    
    
    

   
   
        
    
    
            
    








#with open('large-file.json',encoding="utf-8") as file:
#    lista = json.load(file)
#
#print(type(lista))


