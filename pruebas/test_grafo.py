import unittest

from estructuras.grafo import Grafo
from servicios.gestion_dependencias import GestionDependencias


class PruebasGrafo(unittest.TestCase):
    def crear_grafo(self):
        grafo = Grafo()
        grafo.agregar_dependencia("Porteria")
        grafo.agregar_dependencia("Biblioteca")
        grafo.agregar_dependencia("Salones")
        grafo.conectar("Porteria", "Biblioteca")
        return grafo

    def test_grafo_nuevo_esta_vacio(self):
        grafo = Grafo()
        self.assertEqual(grafo.consultar_dependencias(), [])

    def test_agregar_dependencias(self):
        grafo = self.crear_grafo()
        self.assertEqual(grafo.consultar_dependencias(), ["Porteria", "Biblioteca", "Salones"])

    def test_no_permite_dependencia_duplicada(self):
        grafo = self.crear_grafo()
        self.assertFalse(grafo.agregar_dependencia("Porteria"))
        self.assertEqual(len(grafo.consultar_dependencias()), 3)

    def test_conexion_funciona_en_ambos_sentidos(self):
        grafo = self.crear_grafo()
        self.assertIn("Biblioteca", grafo.consultar_vecinos("Porteria"))
        self.assertIn("Porteria", grafo.consultar_vecinos("Biblioteca"))

    def test_no_permite_conexion_duplicada(self):
        grafo = self.crear_grafo()
        self.assertFalse(grafo.conectar("Porteria", "Biblioteca"))
        self.assertFalse(grafo.conectar("Biblioteca", "Porteria"))
        self.assertEqual(grafo.consultar_vecinos("Porteria"), ["Biblioteca"])

    def test_no_conecta_dependencia_inexistente(self):
        grafo = self.crear_grafo()
        self.assertFalse(grafo.conectar("Porteria", "Laboratorio"))
        self.assertFalse(grafo.conectar("Laboratorio", "Porteria"))

    def test_no_conecta_una_dependencia_consigo_misma(self):
        grafo = self.crear_grafo()
        self.assertFalse(grafo.conectar("Salones", "Salones"))

    def test_vecinos_de_dependencia_sin_conexiones(self):
        grafo = self.crear_grafo()
        self.assertEqual(grafo.consultar_vecinos("Salones"), [])

    def test_vecinos_de_dependencia_inexistente(self):
        grafo = self.crear_grafo()
        self.assertEqual(grafo.consultar_vecinos("Laboratorio"), [])


class PruebasGestionDependencias(unittest.TestCase):
    def test_usa_el_grafo_recibido(self):
        grafo = Grafo()
        gestion = GestionDependencias(grafo)
        gestion.agregar_dependencia("Porteria")
        self.assertTrue(grafo.existe_dependencia("Porteria"))

    def test_contadores(self):
        gestion = GestionDependencias()
        self.assertEqual(gestion.cantidad_dependencias(), 0)
        self.assertEqual(gestion.cantidad_conexiones(), 0)
        gestion.agregar_dependencia("A")
        gestion.agregar_dependencia("B")
        gestion.agregar_dependencia("C")
        gestion.conectar("A", "B")
        gestion.conectar("B", "C")
        self.assertEqual(gestion.cantidad_dependencias(), 3)
        self.assertEqual(gestion.cantidad_conexiones(), 2)

    def test_listar_dependencias(self):
        gestion = GestionDependencias()
        gestion.agregar_dependencia("A")
        gestion.agregar_dependencia("B")
        self.assertEqual(gestion.listar_dependencias(), ["A", "B"])


if __name__ == "__main__":
    unittest.main()
