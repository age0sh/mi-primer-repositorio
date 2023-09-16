# Matrices para almacenar nombres de usuario y contraseñas
matriz_user = [["" for _ in range(10)] for _ in range(10)]
matriz_pass = [["" for _ in range(8)] for _ in range(10)]

# Listas para almacenar respuestas de seguridad
respuestas_numero = [[] for _ in range(10)]
respuestas_hogar = [[] for _ in range(10)]

# Índice del último usuario registrado
ultimo_indice = -1  

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
        return
    respuesta_hogar = input("¿Dónde naciste?: ")
    if not respuesta_hogar.isalpha():
        print("La respuesta debe ser una palabra")
        return
    
    # Almacenar respuestas de seguridad
    respuestas_numero[ultimo_indice].append(respuesta_numero)
    respuestas_hogar[ultimo_indice].append(respuesta_hogar)
    
    print("Usuario registrado exitosamente\n")

#funcion para iniciar sesion
def login():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    for i in range(ultimo_indice + 1):
        if "".join(matriz_user[i]).strip() == usuario and "".join(matriz_pass[i]).strip() == contraseña:
            print("Inicio de sesión exitoso")
            submenu()
            return  # Salir de la función si el inicio de sesión es exitoso
    print("Usuario o contraseña incorrectos")

#funcion para el submenu dentro de iniciar sesion
def submenu():
    while True:
        print("\nBienvenido al sistema de registro de usuarios")
        print("1. Ver datos")
        print("2. Cambiar contraseña")
        print("3. Cerrar sesión")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            verdatos()
        elif opcion == "2":
            cambiarcontraseña()
        elif opcion == "3":
            return  # Salir del submenú
        else:
            print("Opción inválida")

#funcion para ver datos
def verdatos():
    print("MATRIZ USUARIO")
    for i in range(10):
        for j in range(10):
            if matriz_user[i][j] != "":
                print(f"[{matriz_user[i][j]}]", end=" ")
            else:
                print("[ ]", end=" ")
        print()
    print("MATRIZ CONTRASEÑA")
    for i in range(10):
        for j in range(8):
            if matriz_pass[i][j] != "":
                print(f"[{matriz_pass[i][j]}]", end=" ")
            else:
                print("[ ]", end=" ")
        print()

    print("Lista de respuestas para número favorito")
    for i in range(10):
        if respuestas_numero[i]:
            print(f"Usuario {i+1}: {respuestas_numero[i]}")
    print("Lista de respuestas para lugar de nacimiento")
    for i in range(10):
        if respuestas_hogar[i]:
            print(f"Usuario {i+1}: {respuestas_hogar[i]}")

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
            else:
                print("La nueva contraseña no cumple con los requisitos.")
        else:
            print("Las respuestas de seguridad no coinciden.")
    else:
        print("Usuario no encontrado.")

#funcion principal
def main():
    global ultimo_indice

    while True:
        print("\nBienvenido al sistema de registro de usuarios")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            registrar()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("Gracias por usar el sistema")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
