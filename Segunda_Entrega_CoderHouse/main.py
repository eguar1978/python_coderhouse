from tienda import register_customer, process_purchase, show_information, get_customer, show_count_clientes, get_total_customers

def main():
    while True:
        print("\nMenú Principal:")
        print("1. Registrar Cliente Nuevo")
        print("2. Registrar Compra a Cliente")
        print("3. Mostrar Información de Todos los Clientes")
        print("4. Salir")
        option = input("Ingrese una opción: ")

        if option == '1':
            name = input("Ingrese nombre del cliente: ")
            mail = input("Ingrese correo del cliente: ")
            address = input("Ingrese dirección del cliente: ")
            phone = input("Ingrese teléfono del cliente: ")
            register_customer(name, mail, address, phone)
            print("Cliente registrado exitosamente.")
        elif option == '2':
            if show_count_clientes() == 0:
                print("No hay clientes registrados.")
            else:
                index = int(input(f"Ingrese el índice del cliente (0 a {get_total_customers()}): "))
                customer = get_customer(index)
                if customer:
                    compra = input("Ingrese detalles de la compra: ")
                    process_purchase(customer, compra)
                    print("Compra registrada exitosamente.")
                else:
                    print("Índice no válido.")
        elif option == '3':
            if show_count_clientes() == 0:
                print("No hay clientes registrados.")
            else:
                show_information()
        elif option == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()

