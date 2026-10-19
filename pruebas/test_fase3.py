import unittest

from modelos.estudiante import Estudiante
from servicios.gestion_estudiantes import GestionEstudiantes
from estructuras.matriz_notas import MatrizNotas


class PruebasFase3(unittest.TestCase):
    def crear_gestion(self):
        gestion = GestionEstudiantes()
        gestion.registrar(Estudiante("E001", "Ana Pérez", 18, "Matemáticas"))
        gestion.registrar(Estudiante("E002", "Luis Díaz", 19, "Sistemas"))
        gestion.registrar(Estudiante("E003", "Marta Ruiz", 20, "Física"))
        return gestion

    def codigos(self, valores):
        return [e.codigo for e in valores]

    def verificar_listas(self, gestion, esperados):
        # Las dos listas deben tener los mismos estudiantes, en ambos sentidos.
        self.assertEqual(self.codigos(gestion.lista_simple.recorrer()), esperados)
        self.assertEqual(self.codigos(gestion.lista_doble.recorrer_adelante()), esperados)
        self.assertEqual(self.codigos(gestion.lista_doble.recorrer_atras()), esperados[::-1])
        self.assertEqual(gestion.lista_simple.tamano, len(esperados))
        self.assertEqual(gestion.lista_doble.tamano, len(esperados))

    # ---------- Búsqueda ----------

    def test_buscar_encuentra_estudiante(self):
        gestion = self.crear_gestion()
        self.assertEqual(gestion.buscar("E002").nombre, "Luis Díaz")
        self.assertEqual(gestion.lista_doble.buscar("E003").nombre, "Marta Ruiz")

    # ---------- Eliminación ----------

    def test_eliminar_cabeza(self):
        gestion = self.crear_gestion()
        self.assertTrue(gestion.eliminar("E001"))
        self.verificar_listas(gestion, ["E002", "E003"])
        self.assertEqual(gestion.lista_simple.cabeza.valor.codigo, "E002")
        self.assertIsNone(gestion.lista_doble.cabeza.anterior)

    def test_eliminar_nodo_del_medio(self):
        gestion = self.crear_gestion()
        self.assertTrue(gestion.eliminar("E002"))
        self.verificar_listas(gestion, ["E001", "E003"])

    def test_eliminar_cola(self):
        gestion = self.crear_gestion()
        self.assertTrue(gestion.eliminar("E003"))
        self.verificar_listas(gestion, ["E001", "E002"])
        self.assertEqual(gestion.lista_simple.cola.valor.codigo, "E002")
        self.assertEqual(gestion.lista_doble.cola.valor.codigo, "E002")
        self.assertIsNone(gestion.lista_simple.cola.siguiente)
        self.assertIsNone(gestion.lista_doble.cola.siguiente)

    def test_eliminar_unico_nodo(self):
        gestion = GestionEstudiantes()
        gestion.registrar(Estudiante("E001", "Ana", 18, "M"))
        self.assertTrue(gestion.eliminar("E001"))
        self.assertTrue(gestion.lista_simple.esta_vacia())
        self.assertTrue(gestion.lista_doble.esta_vacia())
        self.assertIsNone(gestion.lista_simple.cola)
        self.assertIsNone(gestion.lista_doble.cola)
        self.assertEqual(gestion.lista_simple.tamano, 0)
        self.assertEqual(gestion.lista_doble.tamano, 0)

    def test_registrar_despues_de_vaciar(self):
        gestion = GestionEstudiantes()
        gestion.registrar(Estudiante("E001", "Ana", 18, "M"))
        gestion.eliminar("E001")
        self.assertTrue(gestion.registrar(Estudiante("E002", "Luis", 19, "S")))
        self.verificar_listas(gestion, ["E002"])

    def test_eliminar_en_lista_vacia(self):
        gestion = GestionEstudiantes()
        self.assertFalse(gestion.eliminar("E001"))
        self.assertFalse(gestion.lista_simple.eliminar("E001"))
        self.assertFalse(gestion.lista_doble.eliminar("E001"))

    def test_eliminar_inexistente(self):
        gestion = self.crear_gestion()
        self.assertFalse(gestion.eliminar("E999"))
        self.verificar_listas(gestion, ["E001", "E002", "E003"])

    def test_eliminar_todos_uno_por_uno(self):
        gestion = self.crear_gestion()
        gestion.eliminar("E002")
        gestion.eliminar("E001")
        gestion.eliminar("E003")
        self.assertEqual(gestion.estudiantes, [])
        self.assertTrue(gestion.lista_simple.esta_vacia())
        self.assertTrue(gestion.lista_doble.esta_vacia())

    # ---------- Matriz de notas ----------

    def crear_gestion_con_notas(self, datos):
        # datos: lista de (codigo, nombre, nota)
        gestion = GestionEstudiantes()
        notas = MatrizNotas()
        notas.definir_asignaturas(1)
        for codigo, nombre, nota in datos:
            gestion.registrar(Estudiante(codigo, nombre, 18, "A"))
            notas.agregar_estudiante()
            posicion = gestion.estudiantes.index(gestion.buscar(codigo))
            notas.registrar_nota(posicion, 0, nota)
        return gestion, notas

    def promedio_de(self, gestion, notas, codigo):
        posicion = gestion.estudiantes.index(gestion.buscar(codigo))
        return notas.calcular_promedio(posicion)

    def test_eliminar_estudiante_conserva_notas_de_los_demas(self):
        gestion, notas = self.crear_gestion_con_notas(
            [("E1", "Ana", 3.0), ("E2", "Luis", 4.0), ("E3", "Marta", 5.0)]
        )
        posicion = gestion.estudiantes.index(gestion.buscar("E2"))
        gestion.eliminar("E2")
        notas.eliminar_estudiante(posicion)

        self.assertEqual(len(notas.matriz), 2)
        self.assertEqual(self.promedio_de(gestion, notas, "E1"), 3.0)
        self.assertEqual(self.promedio_de(gestion, notas, "E3"), 5.0)

    def test_ordenar_conserva_nota_de_cada_estudiante(self):
        gestion, notas = self.crear_gestion_con_notas(
            [("E1", "Zoe", 5.0), ("E2", "Ana", 3.0), ("E3", "Luis", 4.0)]
        )
        orden = gestion.ordenar_por_nombre()
        notas.reordenar(orden)

        self.assertEqual(self.codigos(gestion.estudiantes), ["E2", "E3", "E1"])
        self.assertEqual(self.promedio_de(gestion, notas, "E2"), 3.0)  # Ana
        self.assertEqual(self.promedio_de(gestion, notas, "E3"), 4.0)  # Luis
        self.assertEqual(self.promedio_de(gestion, notas, "E1"), 5.0)  # Zoe


if __name__ == "__main__":
    unittest.main()