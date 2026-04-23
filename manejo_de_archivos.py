import json

# 1. Escribir tareas iniciales en archivo
def escribir_tareas(nombre_archivo):
    tareas = [
        "Hacer la tarea de matemáticas",
        "Estudiar para el examen",
        "Lavar los platos",
        "Hacer ejercicio",
        "Leer un libro"
    ]
    
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

# 2. Leer y mostrar tareas numeradas
def leer_tareas(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        tareas = archivo.readlines()
    
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea.strip()}")
    
    return [t.strip() for t in tareas]

# 3. Agregar nuevas tareas
def agregar_tarea(nombre_archivo):
    nueva = input("\nEscribe una nueva tarea: ")
    
    with open(nombre_archivo, "a", encoding="utf-8") as archivo:
        archivo.write(nueva + "\n")

# Bonus: guardar en JSON
def guardar_json(nombre_json, lista_tareas):
    datos = [{"tarea": t, "completada": False} for t in lista_tareas]
    
    with open(nombre_json, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

# Programa principal
def main():
    archivo_txt = "tareas.txt"
    archivo_json = "tareas.json"
    
    # Paso 1
    escribir_tareas(archivo_txt)
    
    # Paso 2
    tareas = leer_tareas(archivo_txt)
    
    # Paso 3
    agregar_tarea(archivo_txt)
    
    # Paso 4
    tareas_actualizadas = leer_tareas(archivo_txt)
    
    print(f"\nTotal de tareas: {len(tareas_actualizadas)}")
    
    # Bonus JSON
    guardar_json(archivo_json, tareas_actualizadas)
    print("\nArchivo JSON creado correctamente.")

# Ejecutar
main()