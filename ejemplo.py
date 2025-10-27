"""
Ejemplo de uso del sistema de registro de fútbol.
Este script demuestra cómo usar las clases Jugador, Equipo y Registro.
"""

from jugador import Jugador
from equipo import Equipo
from registro import Registro


def main():
    """Función principal que demuestra el uso del sistema."""
    
    print("=" * 80)
    print("SISTEMA DE REGISTRO DE EQUIPOS Y JUGADORES DE FÚTBOL")
    print("=" * 80)
    print()
    
    # Crear registro
    registro = Registro()
    
    # Crear equipos
    print("Creando equipos...")
    barcelona = Equipo("FC Barcelona", "Barcelona")
    real_madrid = Equipo("Real Madrid", "Madrid")
    atletico = Equipo("Atlético Madrid", "Madrid")
    print("✓ Equipos creados\n")
    
    # Agregar jugadores al Barcelona
    print("Agregando jugadores al Barcelona...")
    messi = Jugador("Lionel Messi", 10, "Delantero")
    iniesta = Jugador("Andrés Iniesta", 8, "Mediocampista")
    pique = Jugador("Gerard Piqué", 3, "Defensa")
    ter_stegen = Jugador("Marc-André ter Stegen", 1, "Portero")
    
    barcelona.agregar_jugador(messi)
    barcelona.agregar_jugador(iniesta)
    barcelona.agregar_jugador(pique)
    barcelona.agregar_jugador(ter_stegen)
    print(f"✓ {len(barcelona.jugadores)} jugadores agregados al Barcelona\n")
    
    # Agregar jugadores al Real Madrid
    print("Agregando jugadores al Real Madrid...")
    ronaldo = Jugador("Cristiano Ronaldo", 7, "Delantero")
    modric = Jugador("Luka Modrić", 10, "Mediocampista")
    ramos = Jugador("Sergio Ramos", 4, "Defensa")
    
    real_madrid.agregar_jugador(ronaldo)
    real_madrid.agregar_jugador(modric)
    real_madrid.agregar_jugador(ramos)
    print(f"✓ {len(real_madrid.jugadores)} jugadores agregados al Real Madrid\n")
    
    # Agregar jugadores al Atlético
    print("Agregando jugadores al Atlético Madrid...")
    griezmann = Jugador("Antoine Griezmann", 7, "Delantero")
    koke = Jugador("Koke", 6, "Mediocampista")
    
    atletico.agregar_jugador(griezmann)
    atletico.agregar_jugador(koke)
    print(f"✓ {len(atletico.jugadores)} jugadores agregados al Atlético Madrid\n")
    
    # Simular estadísticas de jugadores
    print("Simulando rendimiento de jugadores...\n")
    
    # Messi marca goles y da asistencias
    messi.marcar_gol()
    messi.marcar_gol()
    messi.marcar_gol()
    messi.dar_asistencia()
    messi.dar_asistencia()
    
    # Ronaldo marca goles
    ronaldo.marcar_gol()
    ronaldo.marcar_gol()
    ronaldo.recibir_tarjeta_amarilla()
    
    # Griezmann marca un gol
    griezmann.marcar_gol()
    griezmann.dar_asistencia()
    
    print(f"Estadísticas de Messi: Puntaje = {messi.obtener_puntaje()}")
    print(f"Estadísticas de Ronaldo: Puntaje = {ronaldo.obtener_puntaje()}")
    print(f"Estadísticas de Griezmann: Puntaje = {griezmann.obtener_puntaje()}\n")
    
    # Mostrar información de un jugador específico
    print("-" * 80)
    print(messi)
    print("-" * 80)
    print()
    
    # Registrar resultados de partidos
    print("Registrando resultados de partidos...\n")
    
    # Barcelona: 2 victorias, 1 empate
    barcelona.registrar_victoria(3, 1)
    barcelona.registrar_victoria(2, 0)
    barcelona.registrar_empate(2, 2)
    
    # Real Madrid: 2 victorias, 1 derrota
    real_madrid.registrar_victoria(4, 2)
    real_madrid.registrar_victoria(1, 0)
    real_madrid.registrar_derrota(1, 2)
    
    # Atlético Madrid: 1 victoria, 1 empate, 1 derrota
    atletico.registrar_victoria(2, 1)
    atletico.registrar_empate(1, 1)
    atletico.registrar_derrota(0, 3)
    
    print("✓ Resultados registrados\n")
    
    # Agregar equipos al registro
    registro.agregar_equipo(barcelona)
    registro.agregar_equipo(real_madrid)
    registro.agregar_equipo(atletico)
    
    # Mostrar información de un equipo
    print("-" * 80)
    print(barcelona)
    print("-" * 80)
    print()
    
    # Mostrar tabla de posiciones
    print(registro.mostrar_tabla_posiciones())
    print()
    
    # Buscar un equipo específico
    print("Buscando equipo 'Real Madrid'...")
    equipo_encontrado = registro.buscar_equipo("Real Madrid")
    if equipo_encontrado:
        print(f"✓ Equipo encontrado: {equipo_encontrado.nombre}")
        print(f"  Puntos: {equipo_encontrado.obtener_puntos()}")
        print(f"  Jugadores: {len(equipo_encontrado.jugadores)}\n")
    
    # Buscar un jugador en un equipo
    print("Buscando jugador #10 en Barcelona...")
    jugador_encontrado = barcelona.buscar_jugador(10)
    if jugador_encontrado:
        print(f"✓ Jugador encontrado: {jugador_encontrado.nombre}")
        print(f"  Posición: {jugador_encontrado.posicion}")
        print(f"  Puntaje: {jugador_encontrado.obtener_puntaje()}\n")
    
    print("=" * 80)
    print("DEMOSTRACIÓN COMPLETADA")
    print("=" * 80)


if __name__ == "__main__":
    main()
