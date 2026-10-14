class GestionEstudiantes:
    def __init__(self):
        # Vector que guarda los objetos Estudiante en memoria.
        self.estudiantes = []

    def registrar(self, estudiante):
        if estudiante.codigo == "" or estudiante.nombre.strip() == "":
            return False
        if estudiante.edad <= 0:
            return False
        if self.buscar(estudiante.codigo) is not None:
            return False
        self.estudiantes.append(estudiante)
        return True

    def buscar(self, codigo):
        # Búsqueda lineal: revisa los estudiantes uno por uno.
        for estudiante in self.estudiantes:
            if estudiante.codigo == codigo:
                return estudiante
        return None

    def mostrar_todos(self):
        if len(self.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return

        print("\nLISTA DE ESTUDIANTES")
        for estudiante in self.estudiantes:
            print(estudiante)

    def ordenar_por_nombre(self):
        # Ordenamiento burbuja para practicar el algoritmo visto en clase.
        n = len(self.estudiantes)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.estudiantes[j].nombre.lower() > self.estudiantes[j + 1].nombre.lower():
                    temporal = self.estudiantes[j]
                    self.estudiantes[j] = self.estudiantes[j + 1]
                    self.estudiantes[j + 1] = temporal
