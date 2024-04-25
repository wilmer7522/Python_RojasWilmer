import json

lista = "large-file.json"

crearEvento=[]
#CreateEvent = []
PushEvent = []
WatchEvent = []
ReleaseEvent = []
PullRequestEvent = []
IssuesEvent = []
ForkEvent = []
GollumEvent = []
IssueCommentEvent = []
DeleteEvent = []
PullRequestReviewCommentEvent = []
CommitCommentEvent = []
MemberEvent = []
PublicEvent = []
with open(lista,encoding="utf-8") as file:#abre o llama el archivo .json y codifica en formato utf-8 
    datos = json.load(file)#crea nueva vaiable para cargar con load()
    
      
    
    
volver = True
while volver:    
    print("==========================================================")    
    print("ingrese el numero de la opcion que desea")
    print("==========================================================")
    print("")
    print("")
    print("(1) Leer Eventos\n(0) Salir")
    


    
        
        
    opt = int(input())
    if opt == 1:
        opt_event = int(input("ingrese su opcion a verificar\n(1) CreateEvent\n(2) PushEvent\n(3) WatchEvent\n(4) ReleaseEvent\n(5) PullRequestEvent\n(6) IssuesEvent\n(7) ForkEvent\n(8) GollumEvent\n(9) IssueCommentEvent\n(10) DeleteEvent\n(11) PullRequestReviewCommentEvent\n(12) CommitCommentEvent\n(13) MemberEvent\n(14) PublicEvent\n "))
        if opt_event ==1:

            for i in range(len(datos)):
                if (datos[i]["type"] == "CreateEvent"):
                    crearEvento.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",crearEvento[q]['id'])
                print("Tipo:",crearEvento[q]['type'])
                print("Actor:")
                print("--------ID:",crearEvento[q]['actor']['id'])
                print("--------login:",crearEvento[q]["actor"]["login"])
                print("--------Gravatar ID:",crearEvento[q]["actor"]["gravatar_id"])
                print("--------url:",crearEvento[q]["actor"]["url"])
                print("--------avatar_url:",crearEvento[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",crearEvento[q]['repo']['id'])
                print("--------name:",crearEvento[q]['repo']['name'])
                print("--------url:",crearEvento[q]['repo']['url'])
                print("--------Public:",crearEvento[q]['public'])
                print("--------created_at:",crearEvento[q]['created_at'])

        elif opt_event == 2:
            for i in range(len(datos)):
                if (datos[i]["type"] == "PushEvent"):
                    PushEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",PushEvent[q]['id'])
                print("Tipo:",PushEvent[q]['type'])
                print("Actor:")
                print("--------ID:",PushEvent[q]['actor']['id'])
                print("--------login:",PushEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",PushEvent[q]["actor"]["gravatar_id"])
                print("--------url:",PushEvent[q]["actor"]["url"])
                print("--------avatar_url:",PushEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",PushEvent[q]['repo']['id'])
                print("--------name:",PushEvent[q]['repo']['name'])
                print("--------url:",PushEvent[q]['repo']['url'])
                print("--------Public:",PushEvent[q]['public'])
                print("--------created_at:",PushEvent[q]['created_at'])
        
        elif opt_event == 3:
            for i in range(len(datos)):
                if (datos[i]["type"] == "WatchEvent"):
                    WatchEvent.append(datos[i])
            
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",WatchEvent[q]['id'])
                print("Tipo:",WatchEvent[q]['type'])
                print("Actor:")
                print("--------ID:",WatchEvent[q]['actor']['id'])
                print("--------login:",WatchEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",WatchEvent[q]["actor"]["gravatar_id"])
                print("--------url:",WatchEvent[q]["actor"]["url"])
                print("--------avatar_url:",WatchEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",WatchEvent[q]['repo']['id'])
                print("--------name:",WatchEvent[q]['repo']['name'])
                print("--------url:",WatchEvent[q]['repo']['url'])
                print("--------Public:",WatchEvent[q]['public'])
                print("--------created_at:",WatchEvent[q]['created_at'])

        elif opt_event == 4:
            for i in range(len(datos)):
                if (datos[i]["type"] == "ReleaseEvent"):
                    ReleaseEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",ReleaseEvent[q]['id'])
                print("Tipo:",ReleaseEvent[q]['type'])
                print("Actor:")
                print("--------ID:",ReleaseEvent[q]['actor']['id'])
                print("--------login:",ReleaseEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",ReleaseEvent[q]["actor"]["gravatar_id"])
                print("--------url:",ReleaseEvent[q]["actor"]["url"])
                print("--------avatar_url:",ReleaseEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",ReleaseEvent[q]['repo']['id'])
                print("--------name:",ReleaseEvent[q]['repo']['name'])
                print("--------url:",ReleaseEvent[q]['repo']['url'])
                print("--------Public:",ReleaseEvent[q]['public'])
                print("--------created_at:",ReleaseEvent[q]['created_at'])
         
        elif opt_event == 5:
            for i in range(len(datos)):
                if (datos[i]["type"] == "PullRequestEvent"):
                    PullRequestEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",PullRequestEvent[q]['id'])
                print("Tipo:",PullRequestEvent[q]['type'])
                print("Actor:")
                print("--------ID:",PullRequestEvent[q]['actor']['id'])
                print("--------login:",PullRequestEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",PullRequestEvent[q]["actor"]["gravatar_id"])
                print("--------url:",PullRequestEvent[q]["actor"]["url"])
                print("--------avatar_url:",PullRequestEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",PullRequestEvent[q]['repo']['id'])
                print("--------name:",PullRequestEvent[q]['repo']['name'])
                print("--------url:",PullRequestEvent[q]['repo']['url'])
                print("--------Public:",PullRequestEvent[q]['public'])
                print("--------created_at:",PullRequestEvent[q]['created_at'])

        elif opt_event == 6:
            for i in range(len(datos)):
                if (datos[i]["type"] == "IssuesEvent"):
                    IssuesEvent.append(datos[i])
                      
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",IssuesEvent[q]['id'])
                print("Tipo:",IssuesEvent[q]['type'])
                print("Actor:")
                print("--------ID:",IssuesEvent[q]['actor']['id'])
                print("--------login:",IssuesEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",IssuesEvent[q]["actor"]["gravatar_id"])
                print("--------url:",IssuesEvent[q]["actor"]["url"])
                print("--------avatar_url:",IssuesEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",IssuesEvent[q]['repo']['id'])
                print("--------name:",IssuesEvent[q]['repo']['name'])
                print("--------url:",IssuesEvent[q]['repo']['url'])
                print("--------Public:",IssuesEvent[q]['public'])
                print("--------created_at:",IssuesEvent[q]['created_at'])

        elif opt_event == 7:
            for i in range(len(datos)):
                if (datos[i]["type"] == "ForkEvent"):
                    ForkEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",ForkEvent[q]['id'])
                print("Tipo:",ForkEvent[q]['type'])
                print("Actor:")
                print("--------ID:",ForkEvent[q]['actor']['id'])
                print("--------login:",ForkEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",ForkEvent[q]["actor"]["gravatar_id"])
                print("--------url:",ForkEvent[q]["actor"]["url"])
                print("--------avatar_url:",ForkEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",ForkEvent[q]['repo']['id'])
                print("--------name:",ForkEvent[q]['repo']['name'])
                print("--------url:",ForkEvent[q]['repo']['url'])
                print("--------Public:",ForkEvent[q]['public'])
                print("--------created_at:",ForkEvent[q]['created_at'])

        elif opt_event == 8:
            for i in range(len(datos)):
                if (datos[i]["type"] == "GollumEvent"):
                    GollumEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",GollumEvent[q]['id'])
                print("Tipo:",GollumEvent[q]['type'])
                print("Actor:")
                print("--------ID:",GollumEvent[q]['actor']['id'])
                print("--------login:",GollumEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",GollumEvent[q]["actor"]["gravatar_id"])
                print("--------url:",GollumEvent[q]["actor"]["url"])
                print("--------avatar_url:",GollumEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",GollumEvent[q]['repo']['id'])
                print("--------name:",GollumEvent[q]['repo']['name'])
                print("--------url:",GollumEvent[q]['repo']['url'])
                print("--------Public:",GollumEvent[q]['public'])
                print("--------created_at:",GollumEvent[q]['created_at'])

        elif opt_event == 9:
            for i in range(len(datos)):
                if (datos[i]["type"] == "IssueCommentEvent"):
                    IssueCommentEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",IssueCommentEvent[q]['id'])
                print("Tipo:",IssueCommentEvent[q]['type'])
                print("Actor:")
                print("--------ID:",IssueCommentEvent[q]['actor']['id'])
                print("--------login:",IssueCommentEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",IssueCommentEvent[q]["actor"]["gravatar_id"])
                print("--------url:",IssueCommentEvent[q]["actor"]["url"])
                print("--------avatar_url:",IssueCommentEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",IssueCommentEvent[q]['repo']['id'])
                print("--------name:",IssueCommentEvent[q]['repo']['name'])
                print("--------url:",IssueCommentEvent[q]['repo']['url'])
                print("--------Public:",IssueCommentEvent[q]['public'])
                print("--------created_at:",IssueCommentEvent[q]['created_at'])

        elif opt_event == 10:
            for i in range(len(datos)):
                if (datos[i]["type"] == "DeleteEvent"):
                    DeleteEvent.append(datos[i])
                      
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",DeleteEvent[q]['id'])
                print("Tipo:",DeleteEvent[q]['type'])
                print("Actor:")
                print("--------ID:",DeleteEvent[q]['actor']['id'])
                print("--------login:",DeleteEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",DeleteEvent[q]["actor"]["gravatar_id"])
                print("--------url:",DeleteEvent[q]["actor"]["url"])
                print("--------avatar_url:",DeleteEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",DeleteEvent[q]['repo']['id'])
                print("--------name:",DeleteEvent[q]['repo']['name'])
                print("--------url:",DeleteEvent[q]['repo']['url'])
                print("--------Public:",DeleteEvent[q]['public'])
                print("--------created_at:",DeleteEvent[q]['created_at'])

        elif opt_event == 11:
            for i in range(len(datos)):
                if (datos[i]["type"] == "PullRequestReviewCommentEvent"):
                    PullRequestReviewCommentEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",PullRequestReviewCommentEvent[q]['id'])
                print("Tipo:",PullRequestReviewCommentEvent[q]['type'])
                print("Actor:")
                print("--------ID:",PullRequestReviewCommentEvent[q]['actor']['id'])
                print("--------login:",PullRequestReviewCommentEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",PullRequestReviewCommentEvent[q]["actor"]["gravatar_id"])
                print("--------url:",PullRequestReviewCommentEvent[q]["actor"]["url"])
                print("--------avatar_url:",PullRequestReviewCommentEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",PullRequestReviewCommentEvent[q]['repo']['id'])
                print("--------name:",PullRequestReviewCommentEvent[q]['repo']['name'])
                print("--------url:",PullRequestReviewCommentEvent[q]['repo']['url'])
                print("--------Public:",PullRequestReviewCommentEvent[q]['public'])
                print("--------created_at:",PullRequestReviewCommentEvent[q]['created_at'])

        elif opt_event == 12:
            for i in range(len(datos)):
                if (datos[i]["type"] == "CommitCommentEvent"):
                    CommitCommentEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",CommitCommentEvent[q]['id'])
                print("Tipo:",CommitCommentEvent[q]['type'])
                print("Actor:")
                print("--------ID:",CommitCommentEvent[q]['actor']['id'])
                print("--------login:",CommitCommentEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",CommitCommentEvent[q]["actor"]["gravatar_id"])
                print("--------url:",CommitCommentEvent[q]["actor"]["url"])
                print("--------avatar_url:",CommitCommentEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",CommitCommentEvent[q]['repo']['id'])
                print("--------name:",CommitCommentEvent[q]['repo']['name'])
                print("--------url:",CommitCommentEvent[q]['repo']['url'])
                print("--------Public:",CommitCommentEvent[q]['public'])
                print("--------created_at:",CommitCommentEvent[q]['created_at'])

        elif opt_event == 13:
            for i in range(len(datos)):
                if (datos[i]["type"] == "MemberEvent"):
                    MemberEvent.append(datos[i])
                        
            for q in range (5):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",MemberEvent[q]['id'])
                print("Tipo:",MemberEvent[q]['type'])
                print("Actor:")
                print("--------ID:",MemberEvent[q]['actor']['id'])
                print("--------login:",MemberEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",MemberEvent[q]["actor"]["gravatar_id"])
                print("--------url:",MemberEvent[q]["actor"]["url"])
                print("--------avatar_url:",MemberEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",MemberEvent[q]['repo']['id'])
                print("--------name:",MemberEvent[q]['repo']['name'])
                print("--------url:",MemberEvent[q]['repo']['url'])
                print("--------Public:",MemberEvent[q]['public'])
                print("--------created_at:",MemberEvent[q]['created_at'])

        elif opt_event == 14:
            for i in range(len(datos)):
                if (datos[i]["type"] == "PublicEvent"):
                    PublicEvent.append(datos[i])
                        
            for q in range(len(PublicEvent)):
                print("#######################")
                print("#### Evento # ",q+1 ,"##")
                print("#######################")
                print("ID: ",PublicEvent[q]['id'])
                print("Tipo:",PublicEvent[q]['type'])
                print("Actor:")
                print("--------ID:",PublicEvent[q]['actor']['id'])
                print("--------login:",PublicEvent[q]["actor"]["login"])
                print("--------Gravatar ID:",PublicEvent[q]["actor"]["gravatar_id"])
                print("--------url:",PublicEvent[q]["actor"]["url"])
                print("--------avatar_url:",PublicEvent[q]["actor"]["avatar_url"])
                print("Repo:")
                print("--------ID:",PublicEvent[q]['repo']['id'])
                print("--------name:",PublicEvent[q]['repo']['name'])
                print("--------url:",PublicEvent[q]['repo']['url'])
                print("--------Public:",PublicEvent[q]['public'])
                print("--------created_at:",PublicEvent[q]['created_at'])

            print("elige una opcion\n(1) Crear\n(2) Actualizar\n(3) Eliminar\n ")
            opt_modif = int(input("ingresa tu opcion: "))
            if opt_modif == 1:
                valor_id = (input("Ingrese la ID a Crear: "))

                if valor_id in datos:
                    
                
                    tipo_evento = input("ingrese nuevo evento: ")#ingresamos el nombre del evento que se guarda en "type"
                    actor_id = input("Ingrese la ID del actor: ")
                    actor_login = input("ingrese login del actor: ")
                    actor_gravatar = input("ingrese el gravatar del actor: ")
                    actor_url = input("Ingrese url de actor: ")
                    actor_avatar_url = input("Ingrese el avatar_url de actor: ")
                    nuevo = {"type": tipo_evento, "actor":{"id": actor_id,"login":actor_login,"gravatar":actor_gravatar,"url":actor_url,"avtar_url":actor_avatar_url}}#se guardan ambos datos en un diccionario
                    datos.append(nuevo)#se pasan los datos del diccionario a datos
                   
                   
                    print(f"Nuevo evento agregado")
                else:
                    print("ID ya existe")
              





        
    #    id_crear = (input("Ingrese ID: "))#ingresamos el id que se va a tipo_evento "id"
    #    tipo_evento = input("ingrese nuevo evento: ")#ingresamos el nombre del evento que se guarda en "type"
    #    nuevo = {"type": tipo_evento, "id": id_crear}#se guardan ambos datos en un diccionario
    #    datos.append(nuevo)#se pasan los datos del diccionario a datos
    #    
    #    
    #    print(f"Nuevo evento llamado {[tipo_evento]} agregado")
        


    elif opt == 2:
        id_crear = (input("Ingrese ID: "))#ingresamos el id que se va a tipo_evento "id"
        tipo_evento = input("ingrese nuevo evento: ")#ingresamos el nombre del evento que se guarda en "type"
        nuevo = {"type": tipo_evento, "id": id_crear}#se guardan ambos datos en un diccionario
        datos.append(nuevo)#se pasan los datos del diccionario a datos
            #    
            #    
        print(f"Nuevo evento llamado {[tipo_evento]} agregado")
        #if datos:
                    
    #        for i in range(len(datos)):
    #            if (datos[i]["type"] == "PublicEvent"):
    #                crearEvento.append(datos[i])
    #                print("")
    #            print(f"eventos{crearEvento[i]["id"] }")
    #            print("")
    #        #tipo = int(input("ingrese lugar del evento"))
            #for i, evento in enumerate(datos,1):#recorre i en toda la lista enumerando cada valor 
            #    print("")
            #    #print(datos[tipo]["type"])            
            #    print(f"numero:{i+1} - ID:{evento["id"]} - Type:{evento["type"]} - Actor:{evento["actor"]} - Repo:{evento["repo"]}")#imprime lista com su respectivo ID
            #    print("")
            #    

    
    elif opt == 3:
        id_act = input("Ingrese el ID del evento que desea actualizar: ")#se pide ingresar el numero de id para buscar y actualizar
        for evento in datos:#recorre evento en los datos que son los que estan todos los diccionarios
            if evento["id"] == id_act: #verifica si el id ingresado esta dentro de el id de evento
                n_tip = input("Ingrese el nuevo tipo de evento: ") #pide ingresar el nuvo nombre del evento de "type"
                evento["type"] = n_tip#pasa lo que se ingreso anteriormente a evento en la clave "type"
                print("Evento actualizado")
                print("")
                #break
        else:
            print("ID no encontrado")
            print("")
            #break
        
    elif opt == 4:
        borrar_id = input("Ingrese el id que desea borrar: ")#pide el id que se desea borrar asociado al evento ("type")
        for evento in datos:#recorre evento en los datos que son los que estan todos los diccionarios
            if evento["id"] == borrar_id:#verifica si el id ingresado esta dentro de el id de evento
                datos.remove(evento) #elimina los datos asociados al id que estan en datos          
            
                print("evento eliminado")
                print("")
                #break
        else:   
            print("ID no existe")
            print("")
            #break

    elif opt == 0:
        print("Terminando el programa...")
        volver = False

with open("eventos.json","w") as outfile:
    json.dump(datos,outfile)
    
    
    
    
    
    
    
    
    
    



  
    
    
    
    

   
   
        
    
    
            
    








#with open('large-file.json',encoding="utf-8") as file:
#    lista = json.load(file)
#
#print(type(lista))


