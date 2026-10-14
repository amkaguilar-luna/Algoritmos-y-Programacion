#Lista Multidimensional -- Control básico de productos --
productos = [
    ["Laptop", 15000],
    ["Mouse", 350],
    ["Teclado", 800],
    ["Monitor", 4500],
    ["Impresora", 3200]
]

opcion = 0

while opcion != 6:

    print("\n--- INVENTARIO DE PRODUCTOS ---")
    print("1. Mostrar productos")
    print("2. Buscar producto")
    print("3. Actualizar precio")
    print("4. Calcular valor total del inventario")
    print("5. Agregar producto")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    match opcion:

        # Mostrar todos los productos
        case 1:
            print("\nLista de productos:")

            # TODO: recorrer la lista productos
            for producto in ___________________:

                print(
                    "Producto:",
                    ___________________,
                    "- Precio: $",
                    ___________________
                )

        # Buscar un producto
        case 2:
            buscar = input("Nombre del producto a buscar: ")

            encontrado = False

            # TODO: recorrer la lista productos
            for producto in ___________________:

                # TODO: comparar el nombre capturado
                if _______________________________:
                    print("Producto encontrado")
                    print("Precio: $", producto[1])
                    encontrado = True

            if not encontrado:
                print("Producto no encontrado")

        # Actualizar precio
        case 3:
            buscar = input("Nombre del producto: ")

            # TODO: recorrer la lista productos
            for producto in ___________________:

                # TODO: verificar si el producto existe
                if _______________________________:

                    nuevo_precio = float(
                        input("Nuevo precio: ")
                    )

                    # TODO: actualizar el precio
                    __________________________

                    print("Precio actualizado")

        # Calcular valor total
        case 4:

            total = 0

            # TODO: recorrer la lista productos
            for producto in ___________________:

                # TODO: acumular los precios
                __________________________

            print("Valor total del inventario: $", total)

        # Agregar producto
        case 5:

            nombre = input("Nombre del producto: ")
            precio = float(input("Precio del producto: "))

            # TODO: agregar el nuevo producto
            _________________________________

            print("Producto agregado")

        # Salir
        case 6:
            print("Fin del programa")

        # Opción inválida
        case _:
            print("Opción no válida")
