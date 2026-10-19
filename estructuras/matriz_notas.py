class MatrizNotas:
    def __init__(self):
        self.matriz = []
        self.asignaturas = 0

    def definir_asignaturas(self, cantidad):
        self.asignaturas = cantidad
        for fila in self.matriz:
            fila.extend([None] * cantidad)

    def agregar_estudiante(self):
        self.matriz.append([None] * self.asignaturas)

    def eliminar_estudiante(self, fila):
        # Quita la fila completa del estudiante; las de abajo suben una posición.
        if fila < 0 or fila >= len(self.matriz):
            return False
        self.matriz.pop(fila)
        return True

    def reordenar(self, posiciones):
        # Acomoda las filas en el nuevo orden que dejó el ordenamiento de estudiantes.
        nueva_matriz = []
        for posicion in posiciones:
            nueva_matriz.append(self.matriz[posicion])
        self.matriz = nueva_matriz
    
    def agregar_estudiante_al_inicio(self):
    # Fila nueva en la posición 0, para que coincida con un estudiante agregado al inicio.
        self.matriz.insert(0, [None] * self.asignaturas)

    def cantidad_asignaturas(self):
        return self.asignaturas

    def registrar_nota(self, fila, columna, nota):
        if fila < 0 or fila >= len(self.matriz):
            return False
        if columna < 0 or columna >= self.asignaturas:
            return False
        if nota < 0 or nota > 5:
            return False
        self.matriz[fila][columna] = nota
        return True

    def calcular_promedio(self, fila):
        notas_validas = []
        for nota in self.matriz[fila]:
            if nota is not None:
                notas_validas.append(nota)

        if len(notas_validas) == 0:
            return None

        suma = 0
        for nota in notas_validas:
            suma += nota
        return suma / len(notas_validas)

    def contar_notas(self):
        contador = 0
        for fila in self.matriz:
            for nota in fila:
                if nota is not None:
                    contador += 1
        return contador

    def mostrar(self, estudiantes):
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return
        if self.asignaturas == 0:
            print("Todavía no se ha definido ninguna asignatura.")
            return

        print("\nMATRIZ DE NOTAS")
        encabezado = "Código | Estudiante"
        for numero in range(1, self.asignaturas + 1):
            encabezado += f" | Asig. {numero}"
        print(encabezado)

        for i in range(len(estudiantes)):
            linea = f"{estudiantes[i].codigo} | {estudiantes[i].nombre}"
            for nota in self.matriz[i]:
                if nota is None:
                    linea += " | --"
                else:
                    linea += f" | {nota:.1f}"
            print(linea)
