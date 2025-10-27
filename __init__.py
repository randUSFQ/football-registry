"""
Football Registry - Sistema de Registro de Equipos y Jugadores de Fútbol

Este paquete proporciona clases para gestionar equipos y jugadores de fútbol,
incluyendo seguimiento de estadísticas, puntajes y tablas de posiciones.

Clases principales:
- Jugador: Representa un jugador de fútbol con sus estadísticas
- Equipo: Representa un equipo de fútbol con su plantilla y resultados
- Registro: Gestiona múltiples equipos y genera tablas de posiciones

Ejemplo de uso:
    from football_registry import Jugador, Equipo, Registro
    
    registro = Registro()
    equipo = Equipo("Barcelona", "Barcelona")
    jugador = Jugador("Messi", 10, "Delantero")
    
    equipo.agregar_jugador(jugador)
    jugador.marcar_gol()
    equipo.registrar_victoria(3, 1)
    
    registro.agregar_equipo(equipo)
    print(registro.mostrar_tabla_posiciones())
"""

from jugador import Jugador
from equipo import Equipo
from registro import Registro

__version__ = "1.0.0"
__author__ = "USFQ"
__all__ = ["Jugador", "Equipo", "Registro"]
