import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from servicios.gestion_solicitudes import GestionSolicitudes
from servicios.gestion_historial import GestionHistorial
from servicios.operaciones_recursivas import contar_solicitudes
from interfaz.menu_fase3 import ejecutar_menu_fase3


class PruebasIntegracion(unittest.TestCase):
    def setUp(self):
        self.solicitudes = GestionSolicitudes()
        self.historial = GestionHistorial()

    def usar_menu(self, entradas):
        # Simula lo que escribe el usuario y devuelve lo que el menú imprime.
        # Toda lista de entradas debe terminar en "0" para salir del menú.
        salida = io.StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
            ejecutar_menu_fase3(self.solicitudes, self.historial)
        return salida.getvalue()

    def test_registrar_solicitud_deja_accion_en_historial(self):
        self.usar_menu(["1", "Ana", "Certificado", "0"])
        self.assertEqual(contar_solicitudes(self.solicitudes.solicitudes), 1)
        self.assertEqual(self.historial.cantidad(), 1)
        self.assertIn("turno 1", self.historial.consultar_ultima())

    def test_se_atiende_primero_al_que_llego_primero(self):
        self.usar_menu(["1", "Ana", "Certificado", "1", "Carlos", "Constancia", "0"])
        salida = self.usar_menu(["2", "0"])
        self.assertIn("Ana", salida)
        self.assertEqual(self.solicitudes.solicitudes.consultar_primero()["nombre"], "Carlos")

    def test_atender_con_cola_vacia(self):
        salida = self.usar_menu(["2", "0"])
        self.assertIn("No hay solicitudes para atender.", salida)
        self.assertEqual(self.historial.cantidad(), 0)

    def test_solicitud_con_datos_vacios_no_se_registra(self):
        salida = self.usar_menu(["1", "", "Certificado", "0"])
        self.assertIn("no pueden estar vacíos", salida)
        self.assertEqual(contar_solicitudes(self.solicitudes.solicitudes), 0)
        self.assertEqual(self.historial.cantidad(), 0)

    def test_turno_no_se_reinicia_al_vaciar_la_cola(self):
        self.usar_menu(["1", "Ana", "A", "2", "1", "Carlos", "B", "0"])
        self.assertEqual(self.solicitudes.solicitudes.consultar_primero()["turno"], 2)

    def test_cola_con_un_solo_elemento(self):
        self.usar_menu(["1", "Ana", "A", "0"])
        self.assertEqual(contar_solicitudes(self.solicitudes.solicitudes), 1)
        self.usar_menu(["2", "0"])
        self.assertEqual(contar_solicitudes(self.solicitudes.solicitudes), 0)

    def test_conteo_recursivo_igual_al_del_servicio(self):
        self.usar_menu(["1", "Ana", "A", "1", "Luis", "B", "1", "Marta", "C", "0"])
        cola = self.solicitudes.solicitudes
        self.assertEqual(contar_solicitudes(cola), cola.numero_elementos())
        self.assertEqual(contar_solicitudes(cola), 3)

    def test_historial_en_orden_lifo_con_las_solicitudes(self):
        self.usar_menu(["1", "Ana", "A", "1", "Carlos", "B", "2", "0"])
        # Acciones en orden: registro de Ana, registro de Carlos, atención de Ana.
        self.assertEqual(self.historial.cantidad(), 3)
        self.assertIn("atendida", self.historial.consultar_ultima())
        self.historial.retirar_ultima()
        self.assertIn("turno 2", self.historial.consultar_ultima())

    def test_historial_vacio(self):
        self.assertIsNone(self.historial.consultar_ultima())
        self.assertIsNone(self.historial.retirar_ultima())
        self.assertEqual(self.historial.cantidad(), 0)

    def test_accion_vacia_no_se_registra(self):
        self.assertFalse(self.historial.registrar_accion("   "))
        self.assertEqual(self.historial.cantidad(), 0)


if __name__ == "__main__":
    unittest.main()