# Diccionario para almacenar usuarios y contraseñas
usuarios = {}

# Registrar usuarios y contrasena en el diccionario
def registrar_usuario():
    try:
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        if nombre_usuario in usuarios:
            print("Ese usuario ya existe.")
            return
        contraseña = input("Ingrese la contraseña: ")
        usuarios[nombre_usuario] = contraseña
        print("Usuario registrado exitosamente.")
    except Exception as e:
        print(f"Ha ocurrido un error al registrar el usuario: {e}")

# Muuestra los usuarios registrados
def mostrar_usuarios():
    try:
        if usuarios:
            print("Usuarios registrados:")
            for nombre_usuario, contraseña in usuarios.items():
                print(f"Usuario: {nombre_usuario}, Contraseña: {contraseña}")
        else:
            print("No hay usuarios registrados.")
    except Exception as e:
        print(f"Ha ocurrido un error al mostrar los usuarios: {e}")

# Iniciar sesion de usuario
def iniciar_sesion():
    try:
        nombre_usuario = input("Ingrese su nombre de usuario: ")
        if nombre_usuario in usuarios:
            contraseña = input("Ingrese su contraseña: ")
            if usuarios[nombre_usuario] == contraseña:
                print("Login exitoso.")
            else:
                print("Contraseña incorrecta.")
        else:
            print("El usuario no existe.")
    except Exception as e:
        print(f"Ha ocurrido un error durante el inicio de sesión: {e}")

# Menu principal del programa, tiene un bucle definido en true hasta que el usuario decida salir
def menu():
    while True:
        try:
            print("\nMenú:")
            print("1. Registrar nuevo usuario")
            print("2. Mostrar todos los usuarios")
            print("3. Iniciar sesión de usuario")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                registrar_usuario()
            elif opcion == '2':
                mostrar_usuarios()
            elif opcion == '3':
                iniciar_sesion()
            elif opcion == '4':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        except Exception as e:
            print(f"Error en el menú principal: {e}")

# Ejecuta el programa y llamando a la funcion menu
menu()
