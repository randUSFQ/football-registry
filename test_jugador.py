"""
Pruebas unitarias para el módulo de jugadores.
"""

import unittest
from jugador import Jugador


class TestJugador(unittest.TestCase):
    """Pruebas para la clase Jugador."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.jugador = Jugador("Lionel Messi", 10, "Delantero")
    
    def test_inicializacion(self):
        """Prueba la inicialización de un jugador."""
        self.assertEqual(self.jugador.nombre, "Lionel Messi")
        self.assertEqual(self.jugador.numero, 10)
        self.assertEqual(self.jugador.posicion, "Delantero")
        self.assertEqual(self.jugador.goles, 0)
        self.assertEqual(self.jugador.asistencias, 0)
        self.assertEqual(self.jugador.tarjetas_amarillas, 0)
        self.assertEqual(self.jugador.tarjetas_rojas, 0)
    
    def test_marcar_gol(self):
        """Prueba que se incrementen los goles correctamente."""
        self.jugador.marcar_gol()
        self.assertEqual(self.jugador.goles, 1)
        self.jugador.marcar_gol()
        self.jugador.marcar_gol()
        self.assertEqual(self.jugador.goles, 3)
    
    def test_dar_asistencia(self):
        """Prueba que se incrementen las asistencias correctamente."""
        self.jugador.dar_asistencia()
        self.assertEqual(self.jugador.asistencias, 1)
        self.jugador.dar_asistencia()
        self.assertEqual(self.jugador.asistencias, 2)
    
    def test_recibir_tarjeta_amarilla(self):
        """Prueba que se incrementen las tarjetas amarillas correctamente."""
        self.jugador.recibir_tarjeta_amarilla()
        self.assertEqual(self.jugador.tarjetas_amarillas, 1)
    
    def test_recibir_tarjeta_roja(self):
        """Prueba que se incrementen las tarjetas rojas correctamente."""
        self.jugador.recibir_tarjeta_roja()
        self.assertEqual(self.jugador.tarjetas_rojas, 1)
    
    def test_obtener_puntaje_solo_goles(self):
        """Prueba el cálculo de puntaje con solo goles."""
        self.jugador.marcar_gol()
        self.jugador.marcar_gol()
        self.assertEqual(self.jugador.obtener_puntaje(), 20)  # 2 goles * 10 puntos
    
    def test_obtener_puntaje_solo_asistencias(self):
        """Prueba el cálculo de puntaje con solo asistencias."""
        self.jugador.dar_asistencia()
        self.jugador.dar_asistencia()
        self.jugador.dar_asistencia()
        self.assertEqual(self.jugador.obtener_puntaje(), 15)  # 3 asistencias * 5 puntos
    
    def test_obtener_puntaje_con_tarjetas(self):
        """Prueba el cálculo de puntaje con tarjetas."""
        self.jugador.marcar_gol()  # +10
        self.jugador.dar_asistencia()  # +5
        self.jugador.recibir_tarjeta_amarilla()  # -2
        self.jugador.recibir_tarjeta_roja()  # -5
        self.assertEqual(self.jugador.obtener_puntaje(), 8)  # 10 + 5 - 2 - 5 = 8
    
    def test_obtener_puntaje_completo(self):
        """Prueba el cálculo de puntaje con todas las estadísticas."""
        self.jugador.marcar_gol()
        self.jugador.marcar_gol()
        self.jugador.marcar_gol()  # 30 puntos
        self.jugador.dar_asistencia()
        self.jugador.dar_asistencia()  # 10 puntos
        self.jugador.recibir_tarjeta_amarilla()  # -2 puntos
        # Total: 30 + 10 - 2 = 38
        self.assertEqual(self.jugador.obtener_puntaje(), 38)
    
    def test_str(self):
        """Prueba la representación en string del jugador."""
        resultado = str(self.jugador)
        self.assertIn("Lionel Messi", resultado)
        self.assertIn("#10", resultado)
        self.assertIn("Delantero", resultado)
    
    def test_repr(self):
        """Prueba la representación técnica del jugador."""
        resultado = repr(self.jugador)
        self.assertIn("Jugador", resultado)
        self.assertIn("Lionel Messi", resultado)


if __name__ == '__main__':
    unittest.main()
