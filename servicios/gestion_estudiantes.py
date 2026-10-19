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
        # Búsqueda lineal: recorre los nodos uno por uno.
        actual = self.lista_simple.cabeza
        while actual is not None:
            if actual.valor.codigo == codigo:
                return actual.valor
            actual = actual.siguiente
        return None

    def mostrar_todos(self):
        if self.lista_simple.esta_vacia():
            print("No hay estudiantes registrados.")
            return

        print("\nLISTA DE ESTUDIANTES")
        actual = self.lista_simple.cabeza
        while actual is not None:
            print(actual.valor)
            actual = actual.siguiente

        print("\nESTRUCTURA DE LAS LISTAS")
        print("Lista simple:", self.lista_simple.mostrar_estructura())
        print("Lista doble :", self.lista_doble.mostrar_estructura())

    def ordenar_por_nombre(self):
        # Ordenamiento burbuja sobre un vector temporal; luego se reconstruyen las listas.
        vector = self.lista_doble.recorrer_adelante()
        n = len(vector)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if vector[j].nombre.lower() > vector[j + 1].nombre.lower():
                    temporal = vector[j]
                    vector[j] = vector[j + 1]
                    vector[j + 1] = temporal

        self.lista_simple = ListaSimple()
        self.lista_doble = ListaDoble()
        for estudiante in vector:
            self.lista_simple.agregar_al_final(estudiante)
            self.lista_doble.agregar_al_final(estudiante)