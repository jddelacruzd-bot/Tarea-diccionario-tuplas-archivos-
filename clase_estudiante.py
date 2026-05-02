class Estudiante:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobado(self):
        return self.promedio() >= 61



if __name__ == "__main__":
    nombre = input("Nombre: ")
    carnet = input("Carnet: ")
    carrera = input("Carrera: ")

    est = Estudiante(nombre, carnet, carrera)

    while True:
        nota = input("Ingrese una nota (o 'fin' para terminar): ")
        if nota.lower() == "fin":
            break
        est.agregar_nota(float(nota))

    print("Promedio:", est.promedio())
    print("¿Aprobado?:", est.aprobado())