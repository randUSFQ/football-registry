"""
Módulo para la gestión del registro de equipos y jugadores.
"""


class Registro:
    """Clase que gestiona el registro de equipos de fútbol."""
    
    def __init__(self):
        """Inicializa un nuevo registro de equipos."""
        self.equipos = []
    
    def agregar_equipo(self, equipo):
        """
        Agrega un equipo al registro.
        
        Args:
            equipo: Instancia de la clase Equipo
        """
        self.equipos.append(equipo)
    
    def eliminar_equipo(self, nombre):
        """
        Elimina un equipo del registro por su nombre.
        
        Args:
            nombre (str): Nombre del equipo
            
        Returns:
            bool: True si se eliminó el equipo, False si no se encontró
        """
        for i, equipo in enumerate(self.equipos):
            if equipo.nombre == nombre:
                self.equipos.pop(i)
                return True
        return False
    
    def buscar_equipo(self, nombre):
        """
        Busca un equipo en el registro por su nombre.
        
        Args:
            nombre (str): Nombre del equipo
            
        Returns:
            Equipo o None: El equipo encontrado o None si no existe
        """
        for equipo in self.equipos:
            if equipo.nombre == nombre:
                return equipo
        return None
    
    def obtener_tabla_posiciones(self):
        """
        Obtiene la tabla de posiciones ordenada por puntos, diferencia de goles
        y goles a favor.
        
        Returns:
            list: Lista de equipos ordenada por posición
        """
        return sorted(
            self.equipos,
            key=lambda e: (
                e.obtener_puntos(),
                e.obtener_diferencia_goles(),
                e.goles_favor
            ),
            reverse=True
        )
    
    def mostrar_tabla_posiciones(self):
        """
        Muestra la tabla de posiciones en formato legible.
        
        Returns:
            str: Tabla de posiciones formateada
        """
        tabla = sorted(
            self.equipos,
            key=lambda e: (
                e.obtener_puntos(),
                e.obtener_diferencia_goles(),
                e.goles_favor
            ),
            reverse=True
        )
        
        resultado = "=" * 80 + "\n"
        resultado += "TABLA DE POSICIONES\n"
        resultado += "=" * 80 + "\n"
        resultado += f"{'Pos':<4} {'Equipo':<20} {'PJ':<4} {'G':<4} {'E':<4} "
        resultado += f"{'P':<4} {'GF':<4} {'GC':<4} {'DIF':<5} {'PTS':<4}\n"
        resultado += "-" * 80 + "\n"
        
        for i, equipo in enumerate(tabla, 1):
            resultado += (
                f"{i:<4} {equipo.nombre:<20} "
                f"{equipo.obtener_partidos_jugados():<4} "
                f"{equipo.partidos_ganados:<4} "
                f"{equipo.partidos_empatados:<4} "
                f"{equipo.partidos_perdidos:<4} "
                f"{equipo.goles_favor:<4} "
                f"{equipo.goles_contra:<4} "
                f"{equipo.obtener_diferencia_goles():<5} "
                f"{equipo.obtener_puntos():<4}\n"
            )
        
        resultado += "=" * 80
        return resultado
    
    def __str__(self):
        """Representación en string del registro."""
        return f"Registro con {len(self.equipos)} equipos"
    
    def __repr__(self):
        """Representación técnica del registro."""
        return f"Registro(equipos={len(self.equipos)})"
