from misFunciones import*

# Bluce principal infinito
while True:

# Menu de opciones
    print("\n***** --- Gestos de tareas de consoletec --- *****\n")
    print("1. Añadir tareas")
    print("2. Ver tareas")
    print("3. Marcar tareas como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("\n")
# Entrada para el usuario   
    opcion = int(input("Introduzca una opción: "))

    print("\n")

# Menu de opciones
    if (opcion == 1 ):
        agregar_tarea(tareas)
    elif (opcion == 2):
        ver_tareas(tareas)
    elif (opcion == 3):
        tarea_completada(tareas)
    elif (opcion == 4):
        eliminar_tarea(tareas)
    elif (opcion == 5):
        print("Gracias por usar el software de consoletec. Desconectando...")
        break
    else:
        print("opcion incorrecta")
