# Agenda de Contactos

agenda = []

# ---------------- FUNCIONES ----------------

def agregar_contacto():
    print("\n--- Agregar Contacto ---")
    
    while True:
        nombre = input("Nombre: ").strip()
        if nombre:
            break
        print("El nombre no puede estar vacío.")

    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }

    agenda.append(contacto)
    print("Contacto agregado correctamente.")


def buscar_contacto():
    print("\n--- Buscar Contacto ---")
    nombre = input("Ingrese el nombre a buscar: ").strip()

    encontrado = False
    for contacto in agenda:
        if contacto.get("nombre", "").lower() == nombre.lower():
            print("\nContacto encontrado:")
            print(f"Nombre: {contacto.get('nombre')}")
            print(f"Teléfono: {contacto.get('telefono')}")
            print(f"Email: {contacto.get('email')}")
            encontrado = True
            break

    if not encontrado:
        print("Contacto no encontrado.")


def mostrar_contactos():
    print("\n--- Lista de Contactos ---")

    if not agenda:
        print("No hay contactos registrados.")
        return

    for i, contacto in enumerate(agenda, start=1):
        print(f"\nContacto {i}:")
        print(f"Nombre: {contacto.get('nombre')}")
        print(f"Teléfono: {contacto.get('telefono')}")
        print(f"Email: {contacto.get('email')}")


def eliminar_contacto():
    print("\n--- Eliminar Contacto ---")
    nombre = input("Ingrese el nombre a eliminar: ").strip()

    for contacto in agenda:
        if contacto.get("nombre", "").lower() == nombre.lower():
            agenda.remove(contacto)
            print("Contacto eliminado correctamente.")
            return

    print("Contacto no encontrado.")


# ---------------- MENÚ PRINCIPAL ----------------

def menu():
    while True:
        print("\n===== AGENDA DE CONTACTOS =====")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            mostrar_contactos()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar programa
menu()