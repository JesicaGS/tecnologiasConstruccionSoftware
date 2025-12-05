from item_decorator import ItemDecorator
from character import Character

class BootsOfSpeedDecorator(ItemDecorator):
    """Botas que aumentan la velocidad"""
    
    def __init__(self, character: Character, speed_bonus: int = 10):
        super().__init__(character)
        self._speed_bonus = speed_bonus
    
    def get_speed(self) -> int:
        return self._character.get_speed() + self._speed_bonus
    
    def get_description(self) -> str:
        return f"{self._character.get_description()} + Botas de Velocidad (+{self._speed_bonus} SPD)"


class ShieldDecorator(ItemDecorator):
    """Escudo que aumenta defensa y reduce velocidad"""
    
    def __init__(self, character: Character, defense_bonus: int = 12, speed_penalty: int = 2):
        super().__init__(character)
        self._defense_bonus = defense_bonus
        self._speed_penalty = speed_penalty
    
    def get_defense(self) -> int:
        return self._character.get_defense() + self._defense_bonus
    
    def get_speed(self) -> int:
        return max(1, self._character.get_speed() - self._speed_penalty)
    
    def get_description(self) -> str:
        return (f"{self._character.get_description()} + Escudo "
                f"(+{self._defense_bonus} DEF, -{self._speed_penalty} SPD)")


class RingOfPowerDecorator(ItemDecorator):
    """Anillo que aumenta todas las estadísticas"""
    
    def __init__(self, character: Character, all_stats_bonus: int = 5):
        super().__init__(character)
        self._bonus = all_stats_bonus
    
    def get_attack(self) -> int:
        return self._character.get_attack() + self._bonus
    
    def get_defense(self) -> int:
        return self._character.get_defense() + self._bonus
    
    def get_speed(self) -> int:
        return self._character.get_speed() + self._bonus
    
    def get_description(self) -> str:
        return (f"{self._character.get_description()} + Anillo de Poder "
                f"(+{self._bonus} a todas las stats)")

