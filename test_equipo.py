"""
Pruebas unitarias para el módulo de equipos.
"""

import unittest
from equipo import Equipo
from jugador import Jugador


class TestEquipo(unittest.TestCase):
    """Pruebas para la clase Equipo."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.equipo = Equipo("Barcelona", "Barcelona")
        self.jugador1 = Jugador("Lionel Messi", 10, "Delantero")
        self.jugador2 = Jugador("Andrés Iniesta", 8, "Mediocampista")
    
    def test_inicializacion(self):
        """Prueba la inicialización de un equipo."""
        self.assertEqual(self.equipo.nombre, "Barcelona")
        self.assertEqual(self.equipo.ciudad, "Barcelona")
        self.assertEqual(len(self.equipo.jugadores), 0)
        self.assertEqual(self.equipo.partidos_ganados, 0)
        self.assertEqual(self.equipo.partidos_empatados, 0)
        self.assertEqual(self.equipo.partidos_perdidos, 0)
        self.assertEqual(self.equipo.goles_favor, 0)
        self.assertEqual(self.equipo.goles_contra, 0)
    
    def test_agregar_jugador(self):
        """Prueba agregar jugadores al equipo."""
        self.equipo.agregar_jugador(self.jugador1)
        self.assertEqual(len(self.equipo.jugadores), 1)
        self.equipo.agregar_jugador(self.jugador2)
        self.assertEqual(len(self.equipo.jugadores), 2)
    
    def test_eliminar_jugador(self):
        """Prueba eliminar un jugador del equipo."""
        self.equipo.agregar_jugador(self.jugador1)
        self.equipo.agregar_jugador(self.jugador2)
        
        resultado = self.equipo.eliminar_jugador(10)
        self.assertTrue(resultado)
        self.assertEqual(len(self.equipo.jugadores), 1)
        
        resultado = self.equipo.eliminar_jugador(99)
        self.assertFalse(resultado)
        self.assertEqual(len(self.equipo.jugadores), 1)
    
    def test_buscar_jugador(self):
        """Prueba buscar un jugador en el equipo."""
        self.equipo.agregar_jugador(self.jugador1)
        self.equipo.agregar_jugador(self.jugador2)
        
        jugador_encontrado = self.equipo.buscar_jugador(10)
        self.assertIsNotNone(jugador_encontrado)
        self.assertEqual(jugador_encontrado.nombre, "Lionel Messi")
        
        jugador_no_encontrado = self.equipo.buscar_jugador(99)
        self.assertIsNone(jugador_no_encontrado)
    
    def test_registrar_victoria(self):
        """Prueba registrar una victoria."""
        self.equipo.registrar_victoria(3, 1)
        self.assertEqual(self.equipo.partidos_ganados, 1)
        self.assertEqual(self.equipo.goles_favor, 3)
        self.assertEqual(self.equipo.goles_contra, 1)
    
    def test_registrar_empate(self):
        """Prueba registrar un empate."""
        self.equipo.registrar_empate(2, 2)
        self.assertEqual(self.equipo.partidos_empatados, 1)
        self.assertEqual(self.equipo.goles_favor, 2)
        self.assertEqual(self.equipo.goles_contra, 2)
    
    def test_registrar_derrota(self):
        """Prueba registrar una derrota."""
        self.equipo.registrar_derrota(1, 3)
        self.assertEqual(self.equipo.partidos_perdidos, 1)
        self.assertEqual(self.equipo.goles_favor, 1)
        self.assertEqual(self.equipo.goles_contra, 3)
    
    def test_obtener_puntos(self):
        """Prueba el cálculo de puntos."""
        self.equipo.registrar_victoria(3, 1)  # 3 puntos
        self.equipo.registrar_victoria(2, 0)  # 3 puntos
        self.equipo.registrar_empate(1, 1)    # 1 punto
        self.equipo.registrar_derrota(0, 2)   # 0 puntos
        self.assertEqual(self.equipo.obtener_puntos(), 7)  # 3 + 3 + 1 = 7
    
    def test_obtener_partidos_jugados(self):
        """Prueba el cálculo de partidos jugados."""
        self.equipo.registrar_victoria(3, 1)
        self.equipo.registrar_empate(2, 2)
        self.equipo.registrar_derrota(1, 3)
        self.assertEqual(self.equipo.obtener_partidos_jugados(), 3)
    
    def test_obtener_diferencia_goles(self):
        """Prueba el cálculo de diferencia de goles."""
        self.equipo.registrar_victoria(3, 1)
        self.equipo.registrar_empate(2, 2)
        self.assertEqual(self.equipo.obtener_diferencia_goles(), 2)  # (3+2) - (1+2) = 2
    
    def test_obtener_diferencia_goles_negativa(self):
        """Prueba el cálculo de diferencia de goles negativa."""
        self.equipo.registrar_derrota(0, 3)
        self.equipo.registrar_derrota(1, 2)
        self.assertEqual(self.equipo.obtener_diferencia_goles(), -4)  # (0+1) - (3+2) = -4
    
    def test_str(self):
        """Prueba la representación en string del equipo."""
        resultado = str(self.equipo)
        self.assertIn("Barcelona", resultado)
        self.assertIn("Puntos", resultado)
    
    def test_repr(self):
        """Prueba la representación técnica del equipo."""
        resultado = repr(self.equipo)
        self.assertIn("Equipo", resultado)
        self.assertIn("Barcelona", resultado)


if __name__ == '__main__':
    unittest.main()
