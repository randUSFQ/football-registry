"""
Módulo para la gestión de equipos de fútbol.
"""


class Equipo:
    """Clase que representa un equipo de fútbol."""
    
    def __init__(self, nombre, ciudad):
        """
        Inicializa un nuevo equipo.
        
        Args:
            nombre (str): Nombre del equipo
            ciudad (str): Ciudad del equipo
        """
        self.nombre = nombre
        self.ciudad = ciudad
        self.jugadores = []
        self.partidos_ganados = 0
        self.partidos_empatados = 0
        self.partidos_perdidos = 0
        self.goles_favor = 0
        self.goles_contra = 0
    
    def agregar_jugador(self, jugador):
        """
        Agrega un jugador al equipo.
        
        Args:
            jugador: Instancia de la clase Jugador
        """
        self.jugadores.append(jugador)
    
    def eliminar_jugador(self, numero):
        """
        Elimina un jugador del equipo por su número.
        
        Args:
            numero (int): Número de camiseta del jugador
            
        Returns:
            bool: True si se eliminó el jugador, False si no se encontró
        """
        for i, jugador in enumerate(self.jugadores):
            if jugador.numero == numero:
                self.jugadores.pop(i)
                return True
        return False
    
    def buscar_jugador(self, numero):
        """
        Busca un jugador en el equipo por su número.
        
        Args:
            numero (int): Número de camiseta del jugador
            
        Returns:
            Jugador o None: El jugador encontrado o None si no existe
        """
        for jugador in self.jugadores:
            if jugador.numero == numero:
                return jugador
        return None
    
    def registrar_victoria(self, goles_favor, goles_contra):
        """
        Registra una victoria del equipo.
        
        Args:
            goles_favor (int): Goles anotados por el equipo
            goles_contra (int): Goles recibidos
        """
        self.partidos_ganados += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
    
    def registrar_empate(self, goles_favor, goles_contra):
        """
        Registra un empate del equipo.
        
        Args:
            goles_favor (int): Goles anotados por el equipo
            goles_contra (int): Goles recibidos
        """
        self.partidos_empatados += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
    
    def registrar_derrota(self, goles_favor, goles_contra):
        """
        Registra una derrota del equipo.
        
        Args:
            goles_favor (int): Goles anotados por el equipo
            goles_contra (int): Goles recibidos
        """
        self.partidos_perdidos += 1
        self.goles_favor += goles_favor
        self.goles_contra += goles_contra
    
    def obtener_puntos(self):
        """
        Calcula los puntos del equipo según el sistema estándar:
        Victoria: 3 puntos
        Empate: 1 punto
        Derrota: 0 puntos
        
        Returns:
            int: Puntos totales del equipo
        """
        return self.partidos_ganados * 3 + self.partidos_empatados * 1
    
    def obtener_partidos_jugados(self):
        """
        Calcula el total de partidos jugados.
        
        Returns:
            int: Total de partidos jugados
        """
        return self.partidos_ganados + self.partidos_empatados + self.partidos_perdidos
    
    def obtener_diferencia_goles(self):
        """
        Calcula la diferencia de goles.
        
        Returns:
            int: Diferencia entre goles a favor y en contra
        """
        return self.goles_favor - self.goles_contra
    
    def __str__(self):
        """Representación en string del equipo."""
        return (f"Equipo: {self.nombre} ({self.ciudad})\n"
                f"Jugadores: {len(self.jugadores)}\n"
                f"Partidos: J:{self.obtener_partidos_jugados()} "
                f"G:{self.partidos_ganados} E:{self.partidos_empatados} "
                f"P:{self.partidos_perdidos}\n"
                f"Goles: GF:{self.goles_favor} GC:{self.goles_contra} "
                f"DIF:{self.obtener_diferencia_goles()}\n"
                f"Puntos: {self.obtener_puntos()}")
    
    def __repr__(self):
        """Representación técnica del equipo."""
        return f"Equipo(nombre='{self.nombre}', ciudad='{self.ciudad}')"
