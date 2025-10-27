"""
Pruebas de integración para el sistema completo.
"""

import unittest
from jugador import Jugador
from equipo import Equipo
from registro import Registro


class TestIntegracion(unittest.TestCase):
    """Pruebas de integración del sistema completo."""
    
    def test_sistema_completo(self):
        """Prueba el flujo completo del sistema."""
        # Crear registro
        registro = Registro()
        
        # Crear equipos
        barcelona = Equipo("Barcelona", "Barcelona")
        real_madrid = Equipo("Real Madrid", "Madrid")
        
        # Crear jugadores para Barcelona
        messi = Jugador("Messi", 10, "Delantero")
        iniesta = Jugador("Iniesta", 8, "Mediocampista")
        
        # Crear jugadores para Real Madrid
        ronaldo = Jugador("Ronaldo", 7, "Delantero")
        modric = Jugador("Modric", 10, "Mediocampista")
        
        # Agregar jugadores a equipos
        barcelona.agregar_jugador(messi)
        barcelona.agregar_jugador(iniesta)
        real_madrid.agregar_jugador(ronaldo)
        real_madrid.agregar_jugador(modric)
        
        # Simular estadísticas de jugadores
        messi.marcar_gol()
        messi.marcar_gol()
        messi.dar_asistencia()
        
        ronaldo.marcar_gol()
        ronaldo.recibir_tarjeta_amarilla()
        
        # Verificar puntajes de jugadores
        self.assertEqual(messi.obtener_puntaje(), 25)  # 2*10 + 1*5 = 25
        self.assertEqual(ronaldo.obtener_puntaje(), 8)  # 1*10 - 1*2 = 8
        
        # Registrar resultados de partidos
        barcelona.registrar_victoria(3, 1)
        barcelona.registrar_victoria(2, 0)
        barcelona.registrar_empate(1, 1)
        
        real_madrid.registrar_victoria(2, 1)
        real_madrid.registrar_derrota(0, 1)
        real_madrid.registrar_derrota(1, 2)
        
        # Verificar puntos de equipos
        self.assertEqual(barcelona.obtener_puntos(), 7)  # 2*3 + 1*1 = 7
        self.assertEqual(real_madrid.obtener_puntos(), 3)  # 1*3 = 3
        
        # Agregar equipos al registro
        registro.agregar_equipo(barcelona)
        registro.agregar_equipo(real_madrid)
        
        # Verificar tabla de posiciones
        tabla = registro.obtener_tabla_posiciones()
        self.assertEqual(len(tabla), 2)
        self.assertEqual(tabla[0].nombre, "Barcelona")
        self.assertEqual(tabla[1].nombre, "Real Madrid")
        
        # Verificar que se puede buscar equipos
        equipo = registro.buscar_equipo("Barcelona")
        self.assertIsNotNone(equipo)
        self.assertEqual(len(equipo.jugadores), 2)
        
        # Verificar que se puede buscar jugadores en equipos
        jugador = barcelona.buscar_jugador(10)
        self.assertIsNotNone(jugador)
        self.assertEqual(jugador.nombre, "Messi")
        self.assertEqual(jugador.goles, 2)
    
    def test_escenario_liga(self):
        """Prueba un escenario completo de una liga."""
        registro = Registro()
        
        # Crear 4 equipos
        equipos = [
            Equipo("Barcelona", "Barcelona"),
            Equipo("Real Madrid", "Madrid"),
            Equipo("Atlético", "Madrid"),
            Equipo("Valencia", "Valencia")
        ]
        
        # Agregar jugadores a cada equipo
        for i, equipo in enumerate(equipos):
            for j in range(1, 4):
                jugador = Jugador(f"Jugador{i}-{j}", j, "Delantero")
                equipo.agregar_jugador(jugador)
        
        # Simular una jornada de liga
        # Barcelona 3 - 1 Real Madrid
        equipos[0].registrar_victoria(3, 1)
        equipos[1].registrar_derrota(1, 3)
        
        # Atlético 2 - 2 Valencia
        equipos[2].registrar_empate(2, 2)
        equipos[3].registrar_empate(2, 2)
        
        # Simular otra jornada
        # Barcelona 0 - 2 Atlético
        equipos[0].registrar_derrota(0, 2)
        equipos[2].registrar_victoria(2, 0)
        
        # Real Madrid 3 - 0 Valencia
        equipos[1].registrar_victoria(3, 0)
        equipos[3].registrar_derrota(0, 3)
        
        # Agregar equipos al registro
        for equipo in equipos:
            registro.agregar_equipo(equipo)
        
        # Verificar tabla de posiciones
        tabla = registro.obtener_tabla_posiciones()
        
        # Verificar que Barcelona y Atlético tienen 3 puntos cada uno
        barcelona_en_tabla = next(e for e in tabla if e.nombre == "Barcelona")
        atletico_en_tabla = next(e for e in tabla if e.nombre == "Atlético")
        
        self.assertEqual(barcelona_en_tabla.obtener_puntos(), 3)
        self.assertEqual(atletico_en_tabla.obtener_puntos(), 4)  # 3 + 1
        
        # Atlético debería estar primero por tener más puntos
        self.assertEqual(tabla[0].nombre, "Atlético")
        
        # Verificar que la tabla se muestra correctamente
        tabla_str = registro.mostrar_tabla_posiciones()
        self.assertIn("TABLA DE POSICIONES", tabla_str)
        self.assertIn("Atlético", tabla_str)
    
    def test_eliminacion_y_busqueda(self):
        """Prueba las funciones de eliminación y búsqueda."""
        registro = Registro()
        equipo = Equipo("Barcelona", "Barcelona")
        
        # Agregar jugadores
        jugador1 = Jugador("Messi", 10, "Delantero")
        jugador2 = Jugador("Iniesta", 8, "Mediocampista")
        jugador3 = Jugador("Piqué", 3, "Defensa")
        
        equipo.agregar_jugador(jugador1)
        equipo.agregar_jugador(jugador2)
        equipo.agregar_jugador(jugador3)
        
        self.assertEqual(len(equipo.jugadores), 3)
        
        # Eliminar un jugador
        eliminado = equipo.eliminar_jugador(8)
        self.assertTrue(eliminado)
        self.assertEqual(len(equipo.jugadores), 2)
        
        # Intentar eliminar un jugador que no existe
        eliminado = equipo.eliminar_jugador(99)
        self.assertFalse(eliminado)
        self.assertEqual(len(equipo.jugadores), 2)
        
        # Buscar jugador existente
        jugador = equipo.buscar_jugador(10)
        self.assertIsNotNone(jugador)
        self.assertEqual(jugador.nombre, "Messi")
        
        # Buscar jugador eliminado
        jugador = equipo.buscar_jugador(8)
        self.assertIsNone(jugador)
        
        # Agregar equipo al registro
        registro.agregar_equipo(equipo)
        
        # Buscar equipo
        equipo_encontrado = registro.buscar_equipo("Barcelona")
        self.assertIsNotNone(equipo_encontrado)
        
        # Eliminar equipo
        eliminado = registro.eliminar_equipo("Barcelona")
        self.assertTrue(eliminado)
        self.assertEqual(len(registro.equipos), 0)
        
        # Intentar buscar equipo eliminado
        equipo_encontrado = registro.buscar_equipo("Barcelona")
        self.assertIsNone(equipo_encontrado)


if __name__ == '__main__':
    unittest.main()
