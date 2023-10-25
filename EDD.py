import os
import json
import atexit  # Necesario para registrar la función de guardado al salir del programa

matriz_user = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]

matriz_pass = [[" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "]]

# Nuevas listas para almacenar respuestas de seguridad
respuestas_hogar = [[] for _ in range(10)]
respuestas_numero = [[] for _ in range(10)]

# Índice del último usuario registrado
ultimo_indice = -1

# Función para limpiar pantalla
def limpiar_pantalla():
    if os.name == "posix":
        # Para sistemas tipo Unix (Linux, macOS)
        os.system("clear")
    else:
        # Para sistemas tipo Windows
        os.system("cls")

# Función para cargar datos desde archivos JSON
def cargar_datos():
    global matriz_user, matriz_pass, respuestas_numero, respuestas_hogar, ultimo_indice

    try:
        with open("matriz_user.json", "r") as f:
            matriz_user = json.load(f)
    except FileNotFoundError:
        matriz_user = [[" "] * 10 for _ in range(10)]  # Matriz vacía si no se encuentra el archivo

    try:
        with open("matriz_pass.json", "r") as f:
            matriz_pass = json.load(f)
    except FileNotFoundError:
        matriz_pass = [[" "] * 8 for _ in range(10)]  # Matriz vacía si no se encuentra el archivo

    try:
        with open("respuestas_numero.json", "r") as f:
            respuestas_numero = json.load(f)
    except FileNotFoundError:
        respuestas_numero = [[] for _ in range(10)]  # Lista vacía si no se encuentra el archivo

    try:
        with open("respuestas_hogar.json", "r") as f:
            respuestas_hogar = json.load(f)
    except FileNotFoundError:
        respuestas_hogar = [[] for _ in range(10)]  # Lista vacía si no se encuentra el archivo

    # Obtener el índice del último usuario registrado
    ultimo_indice = -1
    for i, row in enumerate(matriz_user):
        if "".join(row).strip() != "":
            ultimo_indice = i

    guardar_datos()

# Función para guardar datos en archivos JSON
def guardar_datos():
    with open("matriz_user.json", "w") as f:
        json.dump(matriz_user, f)

    with open("matriz_pass.json", "w") as f:
        json.dump(matriz_pass, f)

    with open("respuestas_numero.json", "w") as f:
        json.dump(respuestas_numero, f)

    with open("respuestas_hogar.json", "w") as f:
        json.dump(respuestas_hogar, f)

# Función para registrar usuario
def registrar():
    global ultimo_indice

    # Verificar si se ha alcanzado el límite de usuarios
    if ultimo_indice == 9:
        print("La matriz está llena. No se pueden registrar más usuarios.")
        input("Presione cualquier tecla para continuar...")
        return

    # Solicitar nombre de usuario
    usuario = input("Ingrese su usuario (máximo 10 caracteres): ")

    # Verificar si el usuario ya existe
    if usuario in ["".join(matriz_user[i]).strip() for i in range(ultimo_indice + 1)]:
        print("El usuario ya existe. Intente con un nombre de usuario diferente.")
        input("Presione cualquier tecla para continuar...")
        return

    if len(usuario) > 10:
        print("Usuario muy largo\n")
        input("Presione cualquier tecla para continuar...")
        return

    # Solicitar contraseña
    contraseña = input("Ingrese su contraseña (obligatoriamente 8 caracteres, una mayúscula, un símbolo y al menos un número): ")

    # Verificar si la contraseña cumple con los requisitos
    if len(contraseña) != 8 or not any(c.isupper() for c in contraseña) or not any(c in "!@#$%^&*()-_+=[]{}|;:'<>,.?/" for c in contraseña) or not any(c.isdigit() for c in contraseña):
        print("La contraseña debe tener 8 caracteres exactos, incluyendo al menos 1 mayúscula, 1 símbolo y 1 número")
        input("Presione cualquier tecla para continuar...")
        return

    # Incrementar el índice del último usuario registrado
    ultimo_indice += 1  

    # Almacenar nombre de usuario y contraseña en las matrices correspondientes
    for j, caracter in enumerate(usuario):
        matriz_user[ultimo_indice][j] = caracter

    for j, caracter in enumerate(contraseña):
        matriz_pass[ultimo_indice][j] = caracter

    print("Preguntas de seguridad")
    respuesta_numero = input("¿Cuál es tu número favorito?: ")
    if not respuesta_numero.isdigit():
        print("La respuesta debe ser un número")
        input("Presione cualquier tecla para continuar...")
        # Revertir el incremento del índice
        ultimo_indice -= 1
        return
    respuesta_hogar = input("¿Dónde naciste?: ")
    if not respuesta_hogar.isalpha():
        print("La respuesta debe ser una palabra")
        input("Presione cualquier tecla para continuar...")
        # Revertir el incremento del índice
        ultimo_indice -= 1
        return

    # Almacenar respuestas de seguridad
    respuestas_numero[ultimo_indice].append(respuesta_numero)
    respuestas_hogar[ultimo_indice].append(respuesta_hogar)
    guardar_datos()


# Función para iniciar sesión
def login():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    for i in range(ultimo_indice + 1):
        if "".join(matriz_user[i]).strip() == usuario and "".join(matriz_pass[i]).strip() == contraseña:
            print("Inicio de sesión exitoso")
            input("Presione cualquier tecla para continuar...")
            submenu()
            return  # Salir de la función si el inicio de sesión es exitoso
    print("Usuario o contraseña incorrectos")
    input("Presione cualquier tecla para continuar...")


# Función para el submenu dentro de iniciar sesión
def submenu():
    limpiar_pantalla()
    while True:
        limpiar_pantalla()
        print("Bienvenido al sistema de registro de usuarios")
        print("1. Ver datos")
        print("2. Cambiar contraseña")
        print("3. Eliminar usuario")
        print("4. Ver ordenamientos")
        print("5. Cerrar sesión")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            limpiar_pantalla()
            verdatos()
        elif opcion == "2":
            limpiar_pantalla()
            cambiarcontraseña()
        elif opcion == "3":
            limpiar_pantalla()
            eliminarusuario()
        elif opcion == "4":
            limpiar_pantalla()
            ordenamientos()
        elif opcion == "5":
            return  # Salir del submenú
        else:
            print("Opción inválida")

# Función para ver datos
def verdatos():
    print("MATRIZ USUARIO")
    for i in range(ultimo_indice + 1):  # Iterar solo hasta el último usuario registrado
        for j in range(10):
            if matriz_user[i][j] != " ":
                print(f"[{matriz_user[i][j]}]", end=" ")
            else:
                print("[ ]", end=" ")
        print()

    print("\nMATRIZ CONTRASEÑA")
    for i in range(ultimo_indice + 1):  # Iterar solo hasta el último usuario registrado
        for j in range(8):
            if matriz_pass[i][j] != " ":
                print(f"[{matriz_pass[i][j]}]", end=" ")
            else:
                print("[ ]", end=" ")
        print()

    print("\nLista de respuestas para número favorito")
    for i in range(ultimo_indice + 1):  # Iterar solo hasta el último usuario registrado
        if respuestas_numero[i]:
            print(f"Usuario {i+1}: {respuestas_numero[i]}")
        else:
            print(f"Usuario {i+1}: []")

    print("\nLista de respuestas para lugar de nacimiento")
    for i in range(ultimo_indice + 1):  # Iterar solo hasta el último usuario registrado
        if respuestas_hogar[i]:
            print(f"Usuario {i+1}: {respuestas_hogar[i]}")
        else:
            print(f"Usuario {i+1}: []")

    input("Presione cualquier tecla para continuar...")
    limpiar_pantalla()

# Función para cambiar contraseña
def cambiarcontraseña():
    global ultimo_indice

    usuario = input("Ingrese su usuario: ")
    
    # Buscar el usuario en la matriz de usuarios
    indice_usuario = None
    for i in range(ultimo_indice + 1):
        if "".join(matriz_user[i]).strip() == usuario:
            indice_usuario = i
            break

    if indice_usuario is not None:
        respuesta_numero = input("Ingrese su número favorito: ")
        respuesta_hogar = input("Ingrese su lugar de nacimiento: ")

        # Verificar si las respuestas coinciden con las almacenadas
        if (
            respuestas_numero[indice_usuario] == [respuesta_numero]
            and respuestas_hogar[indice_usuario] == [respuesta_hogar]
        ):
            nueva_contraseña = input("Ingrese su nueva contraseña: ")

            # Verificar la nueva contraseña
            if (
                len(nueva_contraseña) == 8
                and any(c.isupper() for c in nueva_contraseña)
                and any(c in "!@#$%^&*()-_+=[]{}|;:'<>,.?/" for c in nueva_contraseña)
                and any(c.isdigit() for c in nueva_contraseña)
            ):
                matriz_pass[indice_usuario] = list(nueva_contraseña)
                print("Contraseña cambiada con éxito.")
                input("Presione cualquier tecla para continuar...")
                
                guardar_datos()
            else:
                print("La nueva contraseña no cumple con los requisitos.")
                input("Presione cualquier tecla para continuar...")
                
        else:
            print("Las respuestas de seguridad no coinciden.")
            input("Presione cualquier tecla para continuar...")
    else:
        print("Usuario no encontrado.")
        limpiar_pantalla()

# Función para eliminar usuario
def eliminarusuario():
    global ultimo_indice

    usuario = input("Ingrese su usuario: ")

    # Buscar el usuario en la lista de usuarios
    indice_usuario = None
    for i, user in enumerate(usuario):
        if user["nombre"] == usuario:
            indice_usuario = i
            break

    if indice_usuario is not None:
        respuesta_numero = input("Ingrese su número favorito: ")
        respuesta_hogar = input("Ingrese su lugar de nacimiento: ")

        # Verificar si las respuestas coinciden con las almacenadas
        if (
            usuario[indice_usuario]["respuestas_numero"] == [respuesta_numero]
            and usuario[indice_usuario]["respuestas_hogar"] == [respuesta_hogar]
        ):
            # Eliminar el usuario de la lista en memoria
            usuario.pop(indice_usuario)
            ultimo_indice -= 1  # Actualizar el índice del último usuario registrado

            print("Usuario eliminado con éxito")
            input("Presione cualquier tecla para continuar...")

            # Actualizar el archivo JSON inmediatamente
            guardar_datos()

        else:
            print("Las respuestas de seguridad no coinciden.")
            input("Presione cualquier tecla para continuar...")
    else:
        print("Usuario no encontrado.")
        input("Presione cualquier tecla para continuar...")



# Función para realizar ordenamientos
def burbuja(arr):
    n = len(arr)
    movimientos = 0
    consultas = 0
    for i in range(n - 1):
        movimientos_pasada = 0  # Contador de movimientos en la pasada actual
        for j in range(n - 1):
            consultas += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movimientos_pasada += 1
        movimientos += movimientos_pasada

        if not movimientos_pasada:
            break

    ordenada = True
    for i in range(n - 1):
        consultas += 1
        if arr[i] > arr[i + 1]:
            ordenada = False
            break

    return movimientos, consultas, ordenada

# Función para ordenamiento burbuja mejorada
def burbuja_mejorada(arr):
    n = len(arr)
    movimientos = 0
    consultas = 0
    for i in range(n - 1):
        swapped = False
        movimientos_pasada = 0  # Contador de movimientos en la pasada actual
        for j in range(0, n - i - 1):
            consultas += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movimientos_pasada += 1
                swapped = True
        movimientos += movimientos_pasada
        if not swapped:
            break
    return movimientos, consultas

def ordenamientos():
    print("Elige uno de los siguientes ordenamientos")
    print("1. Burbuja")
    print("2. Burbuja mejorada")
    print("3. Volver al menú anterior")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        limpiar_pantalla()
        numeros = input("Ingrese la lista de números separados por comas: ")
        numeros = [int(x) for x in numeros.split(",")]

        movimientos, consultas, ordenada = burbuja(numeros)
        print("Lista ordenada:", numeros)
        print(f"Número de movimientos realizados: {movimientos}")
        print(f"Número de comparaciones realizadas: {consultas}")
        input("presione cualquier tecla para continuar")
    elif opcion == "2":
        limpiar_pantalla()
        numeros = input("Ingrese la lista de números separados por comas: ")
        numeros = [int(x) for x in numeros.split(",")]

        movimientos, consultas = burbuja_mejorada(numeros)
        print("Lista ordenada:", numeros)
        print(f"Número de movimientos realizados: {movimientos}")
        print(f"Número de comparaciones realizadas: {consultas}")
        input("presione cualquier tecla para continuar")

#funcion para ordenamiento burbuja mejorada

# Función principal
def main():
    cargar_datos()
    atexit.register(guardar_datos)  # Registrar la función de guardado al salir del programa

    while True:
        limpiar_pantalla()
        print("Bienvenido al sistema de registro de usuarios")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            registrar()
        elif opcion == "2":
            limpiar_pantalla()
            login()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

   
   

if __name__ == "__main__":
    main()
