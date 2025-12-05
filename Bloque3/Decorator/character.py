from abc import ABC, abstractmethod

class Character(ABC):
    """Interfaz base para el personaje"""
    
    @abstractmethod
    def get_attack(self) -> int:
        """Retorna el ataque del personaje"""
        pass
    
    @abstractmethod
    def get_defense(self) -> int:
        """Retorna la defensa del personaje"""
        pass
    
    @abstractmethod
    def get_speed(self) -> int:
        """Retorna la velocidad del personaje"""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Retorna la descripción del personaje con sus items"""
        pass