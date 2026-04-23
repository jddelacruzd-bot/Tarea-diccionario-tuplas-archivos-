import json

inventario = []

# ---------------- FUNCIONES ----------------

def agregar_producto():
    print("\n--- Agregar Producto ---")

    nombre = input("Nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
    except ValueError:
        print("Error: precio o cantidad inválidos.")
        return

    categoria = input("Categoría: ").strip()

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")


def buscar_producto():
    print("\n--- Buscar Producto ---")
    criterio = input("Buscar por (nombre/categoria): ").strip().lower()
    valor = input("Ingrese el valor: ").strip().lower()

    encontrados = []

    for producto in inventario:
        if criterio == "nombre" and producto.get("nombre", "").lower() == valor:
            encontrados.append(producto)
        elif criterio == "categoria" and producto.get("categoria", "").lower() == valor:
            encontrados.append(producto)

    if encontrados:
        for p in encontrados:
            print(f"\nNombre: {p.get('nombre')}")
            print(f"Precio: {p.get('precio')}")
            print(f"Cantidad: {p.get('cantidad')}")
            print(f"Categoría: {p.get('categoria')}")
    else:
        print("No se encontraron productos.")


def actualizar_cantidad():
    print("\n--- Actualizar Cantidad ---")
    nombre = input("Nombre del producto: ").strip().lower()

    for producto in inventario:
        if producto.get("nombre", "").lower() == nombre:
            try:
                cambio = int(input("Cantidad a agregar (+) o vender (-): "))
            except ValueError:
                print("Entrada inválida.")
                return

            nueva_cantidad = producto.get("cantidad", 0) + cambio

            if nueva_cantidad < 0:
                print("No hay suficiente stock.")
                return

            producto["cantidad"] = nueva_cantidad
            print("Cantidad actualizada.")
            return

    print("Producto no encontrado.")


def valor_total():
    total = 0
    for producto in inventario:
        total += producto.get("precio", 0) * producto.get("cantidad", 0)

    print(f"\nValor total del inventario: Q{total:.2f}")


def stock_bajo():
    print("\n--- Productos con stock bajo (<5) ---")
    bajos = [p for p in inventario if p.get("cantidad", 0) < 5]

    if bajos:
        for p in bajos:
            print(f"{p.get('nombre')} - Cantidad: {p.get('cantidad')}")
    else:
        print("No hay productos con stock bajo.")


def exportar_json():
    print("\n--- Inventario en JSON ---")
    json_string = json.dumps(inventario, indent=4, ensure_ascii=False)
    print(json_string)


# ---------------- MENÚ ----------------

def menu():
    while True:
        print("\n===== INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar cantidad")
        print("4. Valor total del inventario")
        print("5. Mostrar stock bajo")
        print("6. Exportar a JSON")
        print("7. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            actualizar_cantidad()
        elif opcion == "4":
            valor_total()
        elif opcion == "5":
            stock_bajo()
        elif opcion == "6":
            exportar_json()
        elif opcion == "7":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")


# Ejecutar
menu()