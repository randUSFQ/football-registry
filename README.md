# Football Registry / Registro de Fútbol

Sistema de gestión para equipos y jugadores de fútbol con seguimiento de puntajes y estadísticas.

## Descripción

Este sistema permite:
- **Registrar equipos** de fútbol con información básica
- **Gestionar jugadores** con sus estadísticas individuales
- **Seguimiento de puntajes** basado en rendimiento (goles, asistencias, tarjetas)
- **Tabla de posiciones** ordenada por puntos, diferencia de goles y goles a favor
- **Registro de resultados** de partidos (victorias, empates, derrotas)

## Características

### Jugadores
- Nombre, número de camiseta y posición
- Estadísticas: goles, asistencias, tarjetas amarillas y rojas
- Sistema de puntaje automático:
  - Goles: +10 puntos
  - Asistencias: +5 puntos
  - Tarjetas amarillas: -2 puntos
  - Tarjetas rojas: -5 puntos

### Equipos
- Nombre y ciudad
- Gestión de jugadores (agregar, eliminar, buscar)
- Registro de resultados de partidos
- Cálculo automático de puntos (3 por victoria, 1 por empate, 0 por derrota)
- Estadísticas: partidos jugados, ganados, empatados, perdidos
- Goles a favor, goles en contra y diferencia de goles

### Registro
- Gestión de múltiples equipos
- Tabla de posiciones automática ordenada por:
  1. Puntos
  2. Diferencia de goles
  3. Goles a favor
- Búsqueda de equipos

## Instalación

```bash
git clone https://github.com/randUSFQ/football-registry.git
cd football-registry
```

No se requieren dependencias externas. El sistema usa solo la biblioteca estándar de Python.

## Uso

### Ejemplo Básico

```python
from jugador import Jugador
from equipo import Equipo
from registro import Registro

# Crear un registro
registro = Registro()

# Crear un equipo
barcelona = Equipo("FC Barcelona", "Barcelona")

# Crear jugadores
messi = Jugador("Lionel Messi", 10, "Delantero")
iniesta = Jugador("Andrés Iniesta", 8, "Mediocampista")

# Agregar jugadores al equipo
barcelona.agregar_jugador(messi)
barcelona.agregar_jugador(iniesta)

# Registrar estadísticas de jugadores
messi.marcar_gol()
messi.marcar_gol()
messi.dar_asistencia()

print(f"Puntaje de Messi: {messi.obtener_puntaje()}")  # 25 puntos

# Registrar resultados de partidos
barcelona.registrar_victoria(3, 1)
barcelona.registrar_empate(2, 2)

# Agregar equipo al registro
registro.agregar_equipo(barcelona)

# Mostrar tabla de posiciones
print(registro.mostrar_tabla_posiciones())
```

### Ejecutar el Ejemplo Completo

```bash
python ejemplo.py
```

Este script demuestra todas las funcionalidades del sistema con datos de ejemplo.

## Pruebas

El sistema incluye una suite completa de pruebas unitarias:

```bash
# Ejecutar todas las pruebas
python -m unittest test_jugador.py test_equipo.py test_registro.py -v

# Ejecutar pruebas individuales
python -m unittest test_jugador.py -v
python -m unittest test_equipo.py -v
python -m unittest test_registro.py -v
```

## Estructura del Proyecto

```
football-registry/
├── jugador.py           # Clase Jugador
├── equipo.py            # Clase Equipo
├── registro.py          # Clase Registro
├── test_jugador.py      # Pruebas para Jugador
├── test_equipo.py       # Pruebas para Equipo
├── test_registro.py     # Pruebas para Registro
├── ejemplo.py           # Ejemplo de uso completo
└── README.md            # Este archivo
```

## API

### Clase Jugador

```python
Jugador(nombre, numero, posicion)
- marcar_gol()
- dar_asistencia()
- recibir_tarjeta_amarilla()
- recibir_tarjeta_roja()
- obtener_puntaje() -> int
```

### Clase Equipo

```python
Equipo(nombre, ciudad)
- agregar_jugador(jugador)
- eliminar_jugador(numero) -> bool
- buscar_jugador(numero) -> Jugador
- registrar_victoria(goles_favor, goles_contra)
- registrar_empate(goles_favor, goles_contra)
- registrar_derrota(goles_favor, goles_contra)
- obtener_puntos() -> int
- obtener_partidos_jugados() -> int
- obtener_diferencia_goles() -> int
```

### Clase Registro

```python
Registro()
- agregar_equipo(equipo)
- eliminar_equipo(nombre) -> bool
- buscar_equipo(nombre) -> Equipo
- obtener_tabla_posiciones() -> list
- mostrar_tabla_posiciones() -> str
```

## Licencia

Este proyecto está disponible bajo la licencia MIT.

## Autor

Desarrollado para USFQ