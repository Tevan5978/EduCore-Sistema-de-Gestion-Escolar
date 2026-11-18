import unittest

from estructuras.grafo import Grafo
from servicios.recorridos_grafo import RecorridosGrafo


class TestGrafoEduCore(unittest.TestCase):
    def setUp(self):
        self.grafo = Grafo()
        self.grafo.agregar_dependencia("Porteria")
        self.grafo.agregar_dependencia("Biblioteca")
        self.grafo.agregar_dependencia("Salones")
        self.grafo.agregar_dependencia("Enfermeria")
        self.grafo.agregar_dependencia("Cafeteria")

        self.grafo.conectar("Porteria", "Biblioteca")
        self.grafo.conectar("Porteria", "Salones")
        self.grafo.conectar("Biblioteca", "Cafeteria")
        self.grafo.conectar("Salones", "Enfermeria")
        self.recorridos = RecorridosGrafo(self.grafo)

    def test_dependencia_existente(self):
        self.assertTrue(self.grafo.existe_dependencia("Porteria"))

    def test_dependencia_duplicada(self):
        self.assertFalse(self.grafo.agregar_dependencia("Porteria"))

    def test_conexion_no_dirigida(self):
        vecinos = self.grafo.consultar_vecinos("Biblioteca")
        self.assertIn("Porteria", vecinos)

    def test_bfs_respeta_el_orden_de_adyacencia(self):
        self.assertEqual(
            self.recorridos.bfs("Porteria"),
            ["Porteria", "Biblioteca", "Salones", "Cafeteria", "Enfermeria"],
        )

    def test_dfs_respeta_el_orden_de_adyacencia(self):
        self.assertEqual(
            self.recorridos.dfs("Porteria"),
            ["Porteria", "Biblioteca", "Cafeteria", "Salones", "Enfermeria"],
        )

    def test_buscar_ruta_minima(self):
        self.assertEqual(
            self.recorridos.buscar_ruta("Porteria", "Enfermeria"),
            ["Porteria", "Salones", "Enfermeria"],
        )

    def test_buscar_ruta_sin_conexion(self):
        self.grafo.agregar_dependencia("Aula")
        self.assertIsNone(
            self.recorridos.buscar_ruta("Aula", "Enfermeria")
        )


if __name__ == "__main__":
    unittest.main()
