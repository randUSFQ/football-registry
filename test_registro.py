"""
Pruebas unitarias para el módulo de registro.
"""

import unittest
from registro import Registro
from equipo import Equipo
from jugador import Jugador


class TestRegistro(unittest.TestCase):
    """Pruebas para la clase Registro."""
    
    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.registro = Registro()
        self.equipo1 = Equipo("Barcelona", "Barcelona")
        self.equipo2 = Equipo("Real Madrid", "Madrid")
        self.equipo3 = Equipo("Atlético Madrid", "Madrid")
    
    def test_inicializacion(self):
        """Prueba la inicialización del registro."""
        self.assertEqual(len(self.registro.equipos), 0)
    
    def test_agregar_equipo(self):
        """Prueba agregar equipos al registro."""
        self.registro.agregar_equipo(self.equipo1)
        self.assertEqual(len(self.registro.equipos), 1)
        self.registro.agregar_equipo(self.equipo2)
        self.assertEqual(len(self.registro.equipos), 2)
    
    def test_eliminar_equipo(self):
        """Prueba eliminar un equipo del registro."""
        self.registro.agregar_equipo(self.equipo1)
        self.registro.agregar_equipo(self.equipo2)
        
        resultado = self.registro.eliminar_equipo("Barcelona")
        self.assertTrue(resultado)
        self.assertEqual(len(self.registro.equipos), 1)
        
        resultado = self.registro.eliminar_equipo("No Existe")
        self.assertFalse(resultado)
        self.assertEqual(len(self.registro.equipos), 1)
    
    def test_buscar_equipo(self):
        """Prueba buscar un equipo en el registro."""
        self.registro.agregar_equipo(self.equipo1)
        self.registro.agregar_equipo(self.equipo2)
        
        equipo_encontrado = self.registro.buscar_equipo("Barcelona")
        self.assertIsNotNone(equipo_encontrado)
        self.assertEqual(equipo_encontrado.nombre, "Barcelona")
        
        equipo_no_encontrado = self.registro.buscar_equipo("No Existe")
        self.assertIsNone(equipo_no_encontrado)
    
    def test_obtener_tabla_posiciones_ordenada_por_puntos(self):
        """Prueba que la tabla se ordene correctamente por puntos."""
        # Equipo 1: 6 puntos (2 victorias)
        self.equipo1.registrar_victoria(3, 1)
        self.equipo1.registrar_victoria(2, 0)
        
        # Equipo 2: 4 puntos (1 victoria, 1 empate)
        self.equipo2.registrar_victoria(2, 1)
        self.equipo2.registrar_empate(1, 1)
        
        # Equipo 3: 3 puntos (1 victoria)
        self.equipo3.registrar_victoria(1, 0)
        
        self.registro.agregar_equipo(self.equipo1)
        self.registro.agregar_equipo(self.equipo2)
        self.registro.agregar_equipo(self.equipo3)
        
        tabla = self.registro.obtener_tabla_posiciones()
        
        self.assertEqual(tabla[0].nombre, "Barcelona")  # 6 puntos
        self.assertEqual(tabla[1].nombre, "Real Madrid")  # 4 puntos
        self.assertEqual(tabla[2].nombre, "Atlético Madrid")  # 3 puntos
    
    def test_obtener_tabla_posiciones_ordenada_por_diferencia_goles(self):
        """Prueba que la tabla use diferencia de goles como desempate."""
        # Ambos equipos con 3 puntos, pero diferente diferencia de goles
        self.equipo1.registrar_victoria(5, 1)  # +4 diferencia
        self.equipo2.registrar_victoria(2, 1)  # +1 diferencia
        
        self.registro.agregar_equipo(self.equipo1)
        self.registro.agregar_equipo(self.equipo2)
        
        tabla = self.registro.obtener_tabla_posiciones()
        
        self.assertEqual(tabla[0].nombre, "Barcelona")  # Mayor diferencia de goles
        self.assertEqual(tabla[1].nombre, "Real Madrid")
    
    def test_obtener_tabla_posiciones_ordenada_por_goles_favor(self):
        """Prueba que la tabla use goles a favor como segundo desempate."""
        # Mismos puntos y diferencia de goles, pero diferente goles a favor
        self.equipo1.registrar_victoria(3, 1)  # +2, 3 GF
        self.equipo2.registrar_victoria(4, 2)  # +2, 4 GF
        
        self.registro.agregar_equipo(self.equipo1)
        self.registro.agregar_equipo(self.equipo2)
        
        tabla = self.registro.obtener_tabla_posiciones()
        
        self.assertEqual(tabla[0].nombre, "Real Madrid")  # Más goles a favor
        self.assertEqual(tabla[1].nombre, "Barcelona")
    
    def test_mostrar_tabla_posiciones(self):
        """Prueba que se muestre la tabla de posiciones correctamente."""
        self.equipo1.registrar_victoria(3, 1)
        self.equipo2.registrar_empate(2, 2)
        
        self.registro.agregar_equipo(self.equipo1)
        self.registro.agregar_equipo(self.equipo2)
        
        resultado = self.registro.mostrar_tabla_posiciones()
        
        self.assertIn("TABLA DE POSICIONES", resultado)
        self.assertIn("Barcelona", resultado)
        self.assertIn("Real Madrid", resultado)
        self.assertIn("PTS", resultado)
    
    def test_str(self):
        """Prueba la representación en string del registro."""
        self.registro.agregar_equipo(self.equipo1)
        resultado = str(self.registro)
        self.assertIn("1 equipos", resultado)
    
    def test_repr(self):
        """Prueba la representación técnica del registro."""
        resultado = repr(self.registro)
        self.assertIn("Registro", resultado)


if __name__ == '__main__':
    unittest.main()
