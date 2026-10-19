from estructuras.lista_simple import ListaSimple
from estructuras.lista_doble import ListaDoble


class GestionEstudiantes:
    def __init__(self):
        # Los estudiantes se guardan en listas enlazadas (nodos), no en un vector.
        # Ambas listas guardan los mismos objetos Estudiante.
        self.lista_simple = ListaSimple()
        self.lista_doble = ListaDoble()

    @property
    def estudiantes(self):
        # Vista en forma de vector (copia) para el menú y la matriz de notas.
        # Se arma recorriendo los nodos de cabeza a cola.
        return self.lista_doble.recorrer_adelante()

    def registrar(self, estudiante, al_inicio=False):
        if estudiante.codigo == "" or estudiante.nombre.strip() == "":
            return False
        if estudiante.edad <= 0:
            return False
        if self.buscar(estudiante.codigo) is not None:
            return False

        if al_inicio:
            self.lista_simple.agregar_al_inicio(estudiante)
            self.lista_doble.agregar_al_inicio(estudiante)
        else:
            self.lista_simple.agregar_al_final(estudiante)
            self.lista_doble.agregar_al_final(estudiante)
        return True

    def buscar(self, codigo):
        return self.lista_simple.buscar(codigo)

    def eliminar(self, codigo):
        # Los mismos objetos están en ambas listas, así que se sacan de las dos.
        if self.lista_simple.buscar(codigo) is None:
            return False
        self.lista_simple.eliminar(codigo)
        self.lista_doble.eliminar(codigo)
        return True

    def mostrar_todos(self):
        if self.lista_simple.esta_vacia():
            print("No hay estudiantes registrados.")
            return

        print("\nLISTA DE ESTUDIANTES (de inicio a fin)")
        for estudiante in self.lista_simple.recorrer():
            print(estudiante)

        print("\nLISTA DE ESTUDIANTES (de fin a inicio)")
        for estudiante in self.lista_doble.recorrer_atras():
            print(estudiante)

        print("\nESTRUCTURA DE LAS LISTAS")
        print("Lista simple:", self.lista_simple.mostrar_estructura())
        print("Lista doble :", self.lista_doble.mostrar_estructura())

    def ordenar_por_nombre(self):
        # Ordenamiento burbuja sobre un vector temporal; luego se reconstruyen las listas.
        vector = self.lista_doble.recorrer_adelante()
        n = len(vector)

        # posiciones[k] guarda de qué lugar original venía el estudiante que hoy está en k.
        # Se mueve igual que el vector, para poder reordenar después la matriz de notas.
        posiciones = []
        for i in range(n):
            posiciones.append(i)

        for i in range(n - 1):
            for j in range(n - 1 - i):
                if vector[j].nombre.lower() > vector[j + 1].nombre.lower():
                    temporal = vector[j]
                    vector[j] = vector[j + 1]
                    vector[j + 1] = temporal

                    temp_pos = posiciones[j]
                    posiciones[j] = posiciones[j + 1]
                    posiciones[j + 1] = temp_pos

        self.lista_simple = ListaSimple()
        self.lista_doble = ListaDoble()
        for estudiante in vector:
            self.lista_simple.agregar_al_final(estudiante)
            self.lista_doble.agregar_al_final(estudiante)

        return posiciones