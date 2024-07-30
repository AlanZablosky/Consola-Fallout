# Lista de tareas
tareas = ["tarea1","tarea2","tarea3"]

# for indece, tarea in enumerate(tareas): # itera en la lista haciendo que cada objeto sea llamado "tarea"
#       print(indece,tarea)               # en cada iteracion de "enumerate" la lee y la muestra

# Funciones de programa
def agregar_tarea(lista):
    # Entrada para la tarea
    tarea = input("Ingrese una tarea: ")
    
    # Añadir la tarea al final de la lista
    lista.append(tarea)
    
    # Informar de tarea añadida
    print("\nSu tarea a sido añadida con exito\n")
    
    # Imprimir la tarea añadida
    print(f"La tarea añadida es: {tarea}.")
    
    # Imforma del numero de tarea
    print(f"La tarea se almaceno en la posición {len(lista)}\n")# len :cuenta le valor de longitud de la lista.

def ver_tareas(lista):
    # Ver tareas / si la lista esta vacia tirara False, de lo contario True.
    if (lista):
        for indice, tarea in enumerate(lista, start=1):
            print(f"{indice}. {tarea}")
        print("--- FIN DEL LISTADO DE TAREAS ---")    
    else:
        print("--- NO HAY TAREAS PENDIENTES ---")

def tarea_completada(lista):
    # Llamamos a la funcion ver_tarea()
    ver_tareas(lista)
    
    # Entrada para que el usuario introduzca una tarea
    completada = int(input("Introduzca el numero de la tarea a marcar como completada: "))
    
    # Condicional para marcar tareas como completadas
    if (completada > 0 and completada <= len(lista)):
        
        # Condicional para evaluar si la terea ya estaba completada
        # Si la tarea ya esta completada
        if "(completada)" in lista[completada - 1]:
            print("La tarea ya esta marcada como completada.")
        else: 
            lista[completada - 1] = lista[completada - 1]+" (completada)"
            print("Se marco la tarea como completada.")
        
        # En cambio, si no esta ...
    # avisar si la opcion elegida es invalida
    else:
        print("Opcion invalida.")

def eliminar_tarea(lista):
    # invoca a ver tareas
    ver_tareas(lista) 
    # Entrada para eliminar una tarea
    eliminar = int(input("Ingrese cual tarea desea eliminar segun su indice: ")) 
    # Eliminar
    if (eliminar > 0) or (eliminar < len(lista)): 
        lista.pop(eliminar-1)
        print("la tarea","(",eliminar-1,"-",lista[eliminar-1],")","a sido eliminar de tareas")
    else:
        print("Opcion Incorrecta...")

# Terminado - 4/6/24