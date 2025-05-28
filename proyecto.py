'''En este proyecto vamos a organizar un administrador de tareas'''


tareas = []

print("Bienvenido al adiministrador de tareas!! \n")

'''Funcion para agregar las tareas '''
def agregar_tareas():
    global tareas
    diccionario_tareas = {"Descripcion" : input("Descripcion de la tarea: "), 
              "Prioridad": input("Prioridad de la tarea: "), 
              "Completada": "No"}
    tareas.append(diccionario_tareas)
    #Creamos fichero para que se guarden las tareas y no se borren al volver a ejecutar 
    with open ('fichero.txt', 'a') as fichero:
        linea = f"{diccionario_tareas['Descripcion']}|{diccionario_tareas['Prioridad']}|{diccionario_tareas['Completada']}\n"
        fichero.write(linea)
    print("Tarea agregada con éxito!!!")
            

def mostrar_tarea():
    try:
        with open('fichero.txt', 'r') as fichero:
            lineas = fichero.readlines()
            if not lineas:
                print("\nNo hay tareas en el archivo\n")
            else:
                print("\n--- Tareas (desde archivo) ---")
                for linea in lineas:
                    descripcion, prioridad, completada = linea.strip().split('|')
                    estado = "✅" if completada == "Si" else "❌"
                    print(f"{descripcion} | Prioridad: {prioridad} | Completada: {estado}")
    except FileNotFoundError:
        print("\nNo se encontraron tareas cargadas\n")

def completada():
    global tareas
    if not tareas:
        print("\nNo hay tareas disponibles.\n")
        return

    # Mostrar tareas pendientes con números
    print("\n--- Tareas Pendientes ---")
    for i, tarea in enumerate(tareas):
        if tarea["Completada"] == "No":
            print(f"{i+1}. {tarea['Descripcion']} | Prioridad: {tarea['Prioridad']} ❌")

    try:
        # Pedir selección
        indice = int(input("\nIngrese el número de la tarea a completar: ")) - 1
        if 0 <= indice < len(tareas):
            if tareas[indice]["Completada"] == "No":
                tareas[indice]["Completada"] = "Si"
                # Actualizar archivo
                with open('fichero.txt', 'w') as f:
                    for t in tareas:
                        f.write(f"{t['Descripcion']}|{t['Prioridad']}|{t['Completada']}\n")
                print(f"\n✅ Tarea '{tareas[indice]['Descripcion']}' marcada como completada.\n")
            else:
                print("\n⚠️ Esa tarea ya estaba completada.\n")
        else:
            print("\n❌ Número de tarea inválido.\n")
    except ValueError:
        print("\n❌ Error: Debes ingresar un número.\n")


def cargar_tareas():
    global tareas
    try:
         with open ('fichero.txt', 'r') as fichero:
             tareas.clear()
             for linea in fichero:
                linea = linea.strip()
                if linea:  # Ignora líneas vacías
                    descripcion, prioridad, completada = linea.split('|')
                    tareas.append({
                        "Descripcion": descripcion,
                        "Prioridad": prioridad,
                        "Completada": completada
                    })
             
    except FileNotFoundError:
        tareas = []


def menu():
    '''Menú principal'''
    while True:
        print("1. Mostrar las tareas: ")
        print("2. Agregar tareas nuevas: ")
        print("3. Idicar que tarea completaste: ")
        print("4. Salir \n")
        opcion = input("Ingresa una opción: ")

        if opcion == "1":
            mostrar_tarea()
        elif opcion == "2":
            agregar_tareas()
        elif opcion == "3":
            completada()
        elif opcion == "4":
            break



    
