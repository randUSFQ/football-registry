"""
Módulo para la gestión de jugadores de fútbol.
"""


class Jugador:
    """Clase que representa un jugador de fútbol."""
    
    def __init__(self, nombre, numero, posicion):
        """
        Inicializa un nuevo jugador.
        
        Args:
            nombre (str): Nombre del jugador
            numero (int): Número de camiseta del jugador
            posicion (str): Posición del jugador en el campo
        """
        self.nombre = nombre
        self.numero = numero
        self.posicion = posicion
        self.goles = 0
        self.asistencias = 0
        self.tarjetas_amarillas = 0
        self.tarjetas_rojas = 0
    
    def marcar_gol(self):
        """Incrementa el contador de goles del jugador."""
        self.goles += 1
    
    def dar_asistencia(self):
        """Incrementa el contador de asistencias del jugador."""
        self.asistencias += 1
    
    def recibir_tarjeta_amarilla(self):
        """Incrementa el contador de tarjetas amarillas del jugador."""
        self.tarjetas_amarillas += 1
    
    def recibir_tarjeta_roja(self):
        """Incrementa el contador de tarjetas rojas del jugador."""
        self.tarjetas_rojas += 1
    
    def obtener_puntaje(self):
        """
        Calcula el puntaje del jugador basado en su rendimiento.
        Goles: 10 puntos cada uno
        Asistencias: 5 puntos cada una
        Tarjetas amarillas: -2 puntos cada una
        Tarjetas rojas: -5 puntos cada una
        
        Returns:
            int: Puntaje total del jugador
        """
        puntaje = (self.goles * 10 + 
                   self.asistencias * 5 - 
                   self.tarjetas_amarillas * 2 - 
                   self.tarjetas_rojas * 5)
        return puntaje
    
    def __str__(self):
        """Representación en string del jugador."""
        return (f"Jugador: {self.nombre} (#{self.numero}) - {self.posicion}\n"
                f"Goles: {self.goles}, Asistencias: {self.asistencias}\n"
                f"Tarjetas Amarillas: {self.tarjetas_amarillas}, "
                f"Tarjetas Rojas: {self.tarjetas_rojas}\n"
                f"Puntaje: {self.obtener_puntaje()}")
    
    def __repr__(self):
        """Representación técnica del jugador."""
        return (f"Jugador(nombre='{self.nombre}', numero={self.numero}, "
                f"posicion='{self.posicion}')")
