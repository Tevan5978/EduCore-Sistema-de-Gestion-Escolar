import unittest

from modelos.estudiante import Estudiante
from servicios.gestion_estudiantes import GestionEstudiantes
from estructuras.matriz_notas import MatrizNotas


class PruebasFase2(unittest.TestCase):
    def crear_gestion(self):
        gestion = GestionEstudiantes()
        gestion.registrar(Estudiante("E002", "Luis Díaz", 19, "Sistemas"))
        gestion.registrar(Estudiante("E003", "Marta Ruiz", 20, "Física"))
        gestion.registrar(Estudiante("E001", "Ana Pérez", 18, "Matemáticas"), al_inicio=True)
        return gestion

    def codigos(self, valores):
        return [e.codigo for e in valores]

    def test_registrar_al_inicio_y_al_final(self):
        gestion = self.crear_gestion()
        self.assertEqual(self.codigos(gestion.lista_simple.recorrer()), ["E001", "E002", "E003"])
        self.assertEqual(self.codigos(gestion.lista_doble.recorrer_adelante()), ["E001", "E002", "E003"])
        self.assertEqual(self.codigos(gestion.lista_doble.recorrer_atras()), ["E003", "E002", "E001"])
        self.assertEqual(len(gestion.estudiantes), 3)

    def test_no_permite_codigo_repetido(self):
        gestion = self.crear_gestion()
        self.assertFalse(gestion.registrar(Estudiante("E001", "Otro", 20, "Química"), al_inicio=True))
        self.assertEqual(len(gestion.estudiantes), 3)

    def test_buscar_inexistente_y_lista_vacia(self):
        self.assertIsNone(GestionEstudiantes().buscar("E001"))
        self.assertIsNone(self.crear_gestion().buscar("E999"))

    def test_ordenar_por_nombre_reconstruye_ambas_listas(self):
        gestion = GestionEstudiantes()
        gestion.registrar(Estudiante("E1", "Zoe", 18, "A"))
        gestion.registrar(Estudiante("E2", "Ana", 18, "A"))
        gestion.registrar(Estudiante("E3", "Marta", 18, "A"))
        gestion.ordenar_por_nombre()
        self.assertEqual(self.codigos(gestion.lista_simple.recorrer()), ["E2", "E3", "E1"])
        self.assertEqual(self.codigos(gestion.lista_doble.recorrer_atras()), ["E1", "E3", "E2"])

    def test_matriz_coincide_con_registro_al_inicio(self):
        gestion = GestionEstudiantes()
        notas = MatrizNotas()
        notas.definir_asignaturas(1)

        gestion.registrar(Estudiante("E002", "Luis", 19, "S"))
        notas.agregar_estudiante()
        gestion.registrar(Estudiante("E001", "Ana", 18, "M"), al_inicio=True)
        notas.agregar_estudiante_al_inicio()

        posicion = gestion.estudiantes.index(gestion.buscar("E001"))
        notas.registrar_nota(posicion, 0, 4.0)
        self.assertEqual(posicion, 0)
        self.assertEqual(notas.calcular_promedio(0), 4.0)
        self.assertIsNone(notas.calcular_promedio(1))


if __name__ == "__main__":
    unittest.main()