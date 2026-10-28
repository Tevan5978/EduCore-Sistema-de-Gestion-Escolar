import unittest

from estructuras.pila import Pila
from servicios.gestion_historial import GestionHistorial


class PruebasPila(unittest.TestCase):
    def test_pila_nueva_esta_vacia(self):
        pila = Pila()
        self.assertTrue(pila.esta_vacia())
        self.assertEqual(pila.tamano, 0)
        self.assertEqual(pila.recorrer(), [])

    def test_desapilar_pila_vacia(self):
        pila = Pila()
        self.assertIsNone(pila.desapilar())
        self.assertEqual(pila.tamano, 0)

    def test_consultar_tope_pila_vacia(self):
        self.assertIsNone(Pila().consultar_tope())

    def test_apilar_un_elemento(self):
        pila = Pila()
        pila.apilar("A")
        self.assertEqual(pila.consultar_tope(), "A")
        self.assertEqual(pila.tamano, 1)
        self.assertFalse(pila.esta_vacia())

    def test_orden_lifo(self):
        pila = Pila()
        pila.apilar("A")
        pila.apilar("B")
        pila.apilar("C")
        self.assertEqual(pila.desapilar(), "C")
        self.assertEqual(pila.desapilar(), "B")
        self.assertEqual(pila.desapilar(), "A")
        self.assertTrue(pila.esta_vacia())

    def test_consultar_tope_no_retira(self):
        pila = Pila()
        pila.apilar("A")
        pila.apilar("B")
        self.assertEqual(pila.consultar_tope(), "B")
        self.assertEqual(pila.tamano, 2)

    def test_recorrer_del_tope_a_la_base(self):
        pila = Pila()
        pila.apilar("A")
        pila.apilar("B")
        pila.apilar("C")
        self.assertEqual(pila.recorrer(), ["C", "B", "A"])

    def test_estructura(self):
        pila = Pila()
        self.assertEqual(pila.mostrar_estructura(), "tope -> None (pila vacía)")
        pila.apilar("A")
        pila.apilar("B")
        self.assertEqual(pila.mostrar_estructura(), "tope -> [B] -> [A] -> None")


class PruebasGestionHistorial(unittest.TestCase):
    def test_ultima_accion_es_la_primera_en_consultarse(self):
        historial = GestionHistorial()
        historial.registrar_accion("Matrícula de Ana")
        historial.registrar_accion("Actualización de nota de Ana")
        self.assertEqual(historial.consultar_ultima(), "Actualización de nota de Ana")
        self.assertEqual(historial.cantidad(), 2)

    def test_retirar_ultima_accion(self):
        historial = GestionHistorial()
        historial.registrar_accion("Matrícula de Ana")
        historial.registrar_accion("Actualización de nota de Ana")
        self.assertEqual(historial.retirar_ultima(), "Actualización de nota de Ana")
        self.assertEqual(historial.consultar_ultima(), "Matrícula de Ana")
        self.assertEqual(historial.cantidad(), 1)

    def test_historial_vacio(self):
        historial = GestionHistorial()
        self.assertIsNone(historial.consultar_ultima())
        self.assertIsNone(historial.retirar_ultima())
        self.assertEqual(historial.cantidad(), 0)

    def test_rechaza_accion_vacia(self):
        historial = GestionHistorial()
        self.assertFalse(historial.registrar_accion("   "))
        self.assertEqual(historial.cantidad(), 0)


if __name__ == "__main__":
    unittest.main()