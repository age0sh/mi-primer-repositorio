import os
import json

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

#guardar matrices en archivos json
with open('matriz_user.json', 'w') as f:
    json.dump(matriz_user, f)

with open('matriz_pass.json', 'w') as f:
    json.dump(matriz_pass, f)

with open('respuestas_hogar.json', 'w') as f:
    json.dump(respuestas_hogar, f)

with open('respuestas_numero.json', 'w') as f:
    json.dump(respuestas_numero, f)

#actualizar informacion en los archivos json
#search for user by username
username_to_delete = input("Ingrese el usuario que desea eliminar: ")
for i, user in enumerate(matriz_user):
    if "".join(user).strip() == username_to_delete:
        print("Usuario encontrado")
        #delete user
        matriz_user.pop(i)
        matriz_pass.pop(i)
        respuestas_numero.pop(i)
        respuestas_hogar.pop(i)
        break

with open('matriz_user.json', 'w') as f:
    json.dump(matriz_user, f)

with open('matriz_pass.json', 'w') as f:
    json.dump(matriz_pass, f)

with open('respuestas_hogar.json', 'w') as f:
    json.dump(respuestas_hogar, f)

with open('respuestas_numero.json', 'w') as f:
    json.dump(respuestas_numero, f)

# Índice del último usuario registrado
ultimo_indice = -1

#funcion para limpiar pantalla
def limpiar_pantalla():
    if os.name == "posix":
        # Para sistemas tipo Unix (Linux, macOS)
        os.system("clear")
    else:
        # Para sistemas tipo Windows
        os.system("cls")


#funcion para registrar usuario
def registrar():
    global ultimo_indice

    # Verificar si se ha alcanzado el límite de usuarios
    if ultimo_indice == 9:
        print("La matriz está llena. No se pueden registrar más usuarios.")
        return

    # Solicitar nombre de usuario
    usuario = input("Ingrese su usuario (máximo 10 caracteres): ")

    # Verificar si el usuario ya existe
    if usuario in ["".join(matriz_user[i]).strip() for i in range(ultimo_indice + 1)]:
        print("El usuario ya existe. Intente con un nombre de usuario diferente.")
        return

    if len(usuario) > 10:
        print("Usuario muy largo\n")
        return

    # Solicitar contraseña
    contraseña = input("Ingrese su contraseña (obligatoriamente 8 caracteres, una mayúscula, un símbolo y al menos un número): ")

    # Verificar si la contraseña cumple con los requisitos
    if len(contraseña) != 8 or not any(c.isupper() for c in contraseña) or not any(c in "!@#$%^&*()-_+=[]{}|;:'<>,.?/" for c in contraseña) or not any(c.isdigit() for c in contraseña):
        print("La contraseña debe tener 8 caracteres exactos, incluyendo al menos 1 mayúscula, 1 símbolo y 1 número")
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
        # Revertir el incremento del índice
        ultimo_indice -= 1
        return
    respuesta_hogar = input("¿Dónde naciste?: ")
    if not respuesta_hogar.isalpha():
        print("La respuesta debe ser una palabra")
        # Revertir el incremento del índice
        ultimo_indice -= 1
        return

    # Almacenar respuestas de seguridad
    respuestas_numero[ultimo_indice].append(respuesta_numero)
    respuestas_hogar[ultimo_indice].append(respuesta_hogar)

    print("Usuario registrado exitosamente")

#funcion para iniciar sesion
def login():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    for i in range(ultimo_indice + 1):
        if "".join(matriz_user[i]).strip() == usuario and "".join(matriz_pass[i]).strip() == contraseña:
            print("Inicio de sesión exitoso")
            input("Presione cualquier tecla para continuar...")
            limpiar_pantalla()
            submenu()
            return  # Salir de la función si el inicio de sesión es exitoso
    print("Usuario o contraseña incorrectos")

#funcion para el submenu dentro de iniciar sesion
def submenu():
    while True:
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

#funcion para ver datos
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

#funcion para cambiar contraseña
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
                limpiar_pantalla()
            else:
                print("La nueva contraseña no cumple con los requisitos.")
                limpiar_pantalla()
        else:
            print("Las respuestas de seguridad no coinciden.")
            limpiar_pantalla()
    else:
        print("Usuario no encontrado.")
        limpiar_pantalla()

def eliminarusuario():
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
            # Eliminar el usuario encontrado utilizando pop
            matriz_user.pop(indice_usuario)
            matriz_pass.pop(indice_usuario)
            respuestas_numero.pop(indice_usuario)
            respuestas_hogar.pop(indice_usuario)
            ultimo_indice -= 1
            print("Usuario eliminado con éxito.")
            input("Presione cualquier tecla para continuar...")
            limpiar_pantalla()
        else:
            print("Las respuestas de seguridad no coinciden.")
    else:
        print("Usuario no encontrado.")

    # Actualizar el índice del último usuario registrado
    if ultimo_indice < 0:
        ultimo_indice = -1


def ordenamientos():
    print("Elige uno de los siguientes ordenamientos")
    print("1. Burbuja")
    print("2. Burbuja mejorada")
    print("3. Insert Sort")
    print("4. Seleccion")
    print("5. Quick Sort")
    print("6. Merge Sort")
    print("7. Volver al menu anterior")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        limpiar_pantalla()
        burbuja()

    elif opcion == "2":
        limpiar_pantalla()
        burbuja_mejorada()

    elif opcion == "3":
        limpiar_pantalla()
        Insert_Sort()

    elif opcion == "4":
        limpiar_pantalla()
        seleccion()

    elif opcion == "5":
        limpiar_pantalla()
        quick_sort()

    elif opcion == "6":
        limpiar_pantalla()
        merge_sort_analysis()

    elif opcion == "7":
        limpiar_pantalla()
        return
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

def burbuja():
    lista = [
        int(x) for x in input(
            "Ingrese una lista de números separados por comas: ").split(",")
    ]
    n = len(lista)
    iteraciones = 0
    movimientos = 0
    consultas = 0

    for i in range(n):
        ordenado = True
        for j in range(n - i - 1):
            iteraciones += 1
            consultas += 2
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                movimientos += 1
                ordenado = False

        if ordenado:
            break

    print(f"Lista ordenada: {lista}")
    print(f"Total de iteraciones: {iteraciones}")
    print(f"Total de movimientos: {movimientos}")
    print(f"Total de consultas: {consultas}")

    input("Presione cualquier tecla para salir...")
    limpiar_pantalla()

def burbuja_mejorada():
    lista = [
        int(x) for x in input(
            "Ingrese una lista de números separados por comas: ").split(",")
    ]
    n = len(lista)
    iteraciones = 0
    movimientos = 0
    consultas = 0

    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):
            iteraciones += 1
            consultas += 2
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
                movimientos += 1
                print(f"Iteración {iteraciones}: {lista}"
                      )  # imprimir iteración actual
        if not intercambio:
            break

    print(f"\nLista ordenada: {lista}")
    print(f"Total de iteraciones: {iteraciones}")
    print(f"Total de movimientos: {movimientos}")
    print(f"Total de consultas: {consultas/n:.1f}")

    input("Presione cualquier tecla para salir...")
    limpiar_pantalla()

def Insert_Sort():
    lista = input("Ingrese una lista de números separados por comas: ").split(
        ",")
    n = len(lista)
    iteraciones = 0
    movimientos = 0
    consultas = 0

    for i in range(1, n):
        actual = lista[i]
        j = i - 1
        while j >= 0 and actual < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
            iteraciones += 1
            movimientos += 1
            consultas += 2
            print(f"Iteración {iteraciones}: {lista}"
                  )  # imprimir iteración actual
        lista[j + 1] = actual
        movimientos += 1
        print(f"Iteración {iteraciones}: {lista}")  # imprimir iteración actual

    print(f"Lista ordenada: {lista}")
    print(f"Total de iteraciones: {iteraciones}")
    print(f"Total de movimientos: {movimientos}")
    print(f"Total de consultas: {consultas}")

    input("Presione cualquier tecla para salir...")
    limpiar_pantalla()


def seleccion():
    lista = input("Ingrese una lista de números separados por comas: ").split(
        ",")
    lista = [int(num) for num in lista]
    n = len(lista)
    iteraciones = 0
    movimientos = 0
    consultas = 0

    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            iteraciones += 1
            consultas += 1
            if lista[j] < lista[minimo]:
                minimo = j
        if minimo != i:
            lista[i], lista[minimo] = lista[minimo], lista[i]
            movimientos += 1

    print(f"consultas: {consultas}")
    print(f"movimientos: {movimientos}")
    print(f"iteraciones: {iteraciones}")
    print(f"lista ordenada: {lista}")

    input("Presione cualquier tecla para salir...")
    limpiar_pantalla()


def quick_sort():
    lista = input("Ingrese una lista de números separados por comas: ").split(
        ",")
    lista = [int(i) for i in lista]  # Convertir elementos a tipo entero
    n = len(lista)
    iteraciones = 0
    movimientos = 0
    consultas = 0

    def ordenar(inicio, fin):
        nonlocal iteraciones, movimientos, consultas
        if inicio >= fin:
            return
        pivote = lista[inicio]
        i, j = inicio + 1, fin
        while i <= j:
            iteraciones += 1
            consultas += 2
            if lista[i] > pivote and lista[j] < pivote:
                lista[i], lista[j] = lista[j], lista[i]
                movimientos += 2
                i += 1
                j -= 1
            elif lista[i] <= pivote:
                i += 1
            elif lista[j] >= pivote:
                j -= 1
        lista[inicio], lista[j] = lista[j], lista[inicio]
        movimientos += 2
        print(f"Iteración {iteraciones}: {lista}")  # Imprimir iteración actual
        ordenar(inicio, j - 1)
        ordenar(j + 1, fin)

    ordenar(0, n - 1)
    print(f"\nLista ordenada: {lista}")
    print(f"Total de iteraciones: {iteraciones}")
    print(f"Total de movimientos: {movimientos}")
    print(f"Total de consultas: {consultas}")

    input("Presione cualquier tecla para salir...")
    limpiar_pantalla()


def merge_sort_analysis():
    # Solicitar al usuario ingresar la lista de números separados por coma
    input_list = input("Ingrese una lista de números separados por coma: ").split(",")
    numbers = [int(num) for num in input_list]

    # Llamar a la función merge_sort() para ordenar la lista y obtener los resultados
    iterations, movements, queries = merge_sort(numbers)

    # Imprimir los resultados
    print("Lista ordenada:", numbers)
    print("Número de iteraciones:", iterations)
    print("Número de movimientos:", movements)
    print("Número de consultas:", queries)

    input("Presione cualquier tecla para salir...")
    limpiar_pantalla()

def merge_sort(arr):
    if len(arr) <= 1:
        return 0, 0, 0

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Realizar recursivamente el ordenamiento en las sublistas izquierda y derecha
    left_iterations, left_movements, left_queries = merge_sort(left_half)
    right_iterations, right_movements, right_queries = merge_sort(right_half)

    # Realizar el proceso de combinación (merge)
    iterations = left_iterations + right_iterations + 1
    movements = left_movements + right_movements + merge(arr, left_half, right_half)
    queries = left_queries + right_queries + 1

    return iterations, movements, queries

def merge(arr, left_half, right_half):
    i = j = k = 0
    movements = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        movements += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        movements += 1
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        movements += 1
        j += 1
        k += 1

    return movements

    

def main():
    global ultimo_indice

    while True:
        limpiar_pantalla()  # Limpia la pantalla antes de mostrar el menú
        print("Bienvenido al sistema de registro de usuarios")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            limpiar_pantalla()  # Limpia la pantalla antes de registrar
            registrar()
            input("Presione Enter para continuar...")
        elif opcion == "2":
            limpiar_pantalla()  # Limpia la pantalla antes de iniciar sesión
            login()
            input("Presione Enter para continuar...")
        elif opcion == "3":
            limpiar_pantalla()
            print("Gracias por usar el sistema. :)")
            break
        else:
            print("Opción inválida")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()
