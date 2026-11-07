import unittest

from modelos.estudiante import Estudiante
from servicios.gestion_arbol_estudiantes import GestionArbolEstudiantes
from estructuras.arbol_binario import ArbolBinario


class PruebasArbolBinario(unittest.TestCase):
    def test_arbol_vacio_y_busqueda_sin_resultados(self):
        arbol = ArbolBinario()

        self.assertTrue(arbol.esta_vacio())
        self.assertEqual(arbol.cantidad, 0)
        self.assertIsNone(arbol.buscar(105))

    def test_insertar_y_buscar_varios_codigos_numericos(self):
        arbol = ArbolBinario()
        estudiantes = [
            (105, "Ana"),
            (102, "Carlos"),
            (108, "Laura"),
            (101, "Pedro"),
            (104, "Maria"),
        ]

        for codigo, nombre in estudiantes:
            self.assertTrue(arbol.insertar(codigo, nombre))

        self.assertFalse(arbol.esta_vacio())
        self.assertEqual(arbol.cantidad, 5)
        self.assertEqual(arbol.buscar(102), "Carlos")
        self.assertIsNone(arbol.buscar(110))

    def test_rechazar_codigo_duplicado_sin_reemplazar_informacion(self):
        arbol = ArbolBinario()

        self.assertTrue(arbol.insertar(105, "Ana"))
        self.assertFalse(arbol.insertar(105, "Otra estudiante"))

        self.assertEqual(arbol.cantidad, 1)
        self.assertEqual(arbol.buscar(105), "Ana")

    def test_admitir_un_solo_nodo(self):
        arbol = ArbolBinario()

        self.assertTrue(arbol.insertar(105, "Ana"))
        self.assertFalse(arbol.esta_vacio())
        self.assertEqual(arbol.cantidad, 1)
        self.assertEqual(arbol.buscar(105), "Ana")

    def test_gestionar_estudiantes_con_codigos_de_texto_del_proyecto(self):
        gestion = GestionArbolEstudiantes()
        estudiante = Estudiante("E001", "Ana Pérez", 18, "Matemáticas")

        self.assertTrue(gestion.insertar(estudiante))
        self.assertFalse(
            gestion.insertar(Estudiante("E001", "Otra estudiante", 19, "Sistemas"))
        )
        self.assertIs(gestion.buscar("E001"), estudiante)
        self.assertIsNone(gestion.buscar("E002"))
        self.assertEqual(gestion.arbol.cantidad, 1)


if __name__ == "__main__":
    unittest.main()
