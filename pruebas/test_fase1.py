import unittest

from modelos.estudiante import Estudiante
from servicios.gestion_estudiantes import GestionEstudiantes
from estructuras.matriz_notas import MatrizNotas


class PruebasFase1(unittest.TestCase):
    def test_registrar_y_buscar_estudiante(self):
        gestion = GestionEstudiantes()
        estudiante = Estudiante("E001", "Ana Pérez", 18, "Matemáticas")
        self.assertTrue(gestion.registrar(estudiante))
        self.assertEqual(gestion.buscar("E001").nombre, "Ana Pérez")

    def test_no_permite_codigo_repetido(self):
        gestion = GestionEstudiantes()
        gestion.registrar(Estudiante("E001", "Ana Pérez", 18, "Matemáticas"))
        self.assertFalse(gestion.registrar(Estudiante("E001", "Luis Díaz", 19, "Sistemas")))

    def test_matriz_y_promedio(self):
        notas = MatrizNotas()
        notas.agregar_estudiante()
        notas.definir_asignaturas(3)
        notas.registrar_nota(0, 0, 4.0)
        notas.registrar_nota(0, 1, 3.0)
        self.assertEqual(notas.calcular_promedio(0), 3.5)

    def test_rechaza_nota_fuera_de_rango(self):
        notas = MatrizNotas()
        notas.agregar_estudiante()
        notas.definir_asignaturas(1)
        self.assertFalse(notas.registrar_nota(0, 0, 6.0))


if __name__ == "__main__":
    unittest.main()
