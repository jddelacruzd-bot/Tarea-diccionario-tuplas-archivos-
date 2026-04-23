import json

# 1. JSON string con 3 cursos
json_string = '''
[
    {
        "nombre": "Programación I",
        "codigo": "CS101",
        "creditos": 4,
        "horario": "Lunes 8:00-10:00",
        "prerequisitos": []
    },
    {
        "nombre": "Matemática Básica",
        "codigo": "MA101",
        "creditos": 3,
        "horario": "Martes 10:00-12:00",
        "prerequisitos": []
    },
    {
        "nombre": "Estructuras de Datos",
        "codigo": "CS201",
        "creditos": 5,
        "horario": "Miércoles 14:00-16:00",
        "prerequisitos": ["CS101"]
    }
]
'''

# 2. Parsear JSON
cursos = json.loads(json_string)

# 3. Imprimir cursos con más de 3 créditos
print("\n--- Cursos con más de 3 créditos ---")
for curso in cursos:
    if curso.get("creditos", 0) > 3:
        print(f"{curso.get('nombre')} ({curso.get('creditos')} créditos)")

# 4. Buscar curso por código
def buscar_por_codigo(codigo):
    for curso in cursos:
        if curso.get("codigo") == codigo:
            return curso
    return None

codigo_buscar = "CS201"
resultado = buscar_por_codigo(codigo_buscar)

print("\n--- Búsqueda por código ---")
if resultado:
    print("Curso encontrado:", resultado)
else:
    print("Curso no encontrado")

# 5. Modificar el horario de un curso
codigo_modificar = "CS101"
for curso in cursos:
    if curso.get("codigo") == codigo_modificar:
        curso["horario"] = "Lunes 9:00-11:00"
        print("\nHorario actualizado para", curso.get("nombre"))

# 6. Convertir de vuelta a JSON
nuevo_json = json.dumps(cursos, indent=4, ensure_ascii=False)

print("\n--- JSON actualizado ---")
print(nuevo_json)

# Bonus: función que recibe código y retorna curso
def obtener_curso(codigo):
    return next((c for c in cursos if c.get("codigo") == codigo), None)

# Ejemplo bonus
print("\n--- Bonus ---")
print(obtener_curso("CS101"))