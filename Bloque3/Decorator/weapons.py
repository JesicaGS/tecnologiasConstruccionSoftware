from item_decorator import ItemDecorator
from character import Character

class SwordDecorator(ItemDecorator):
    """Espada que aumenta el ataque"""
    
    def __init__(self, character: Character, damage_bonus: int = 15):
        super().__init__(character)
        self._damage_bonus = damage_bonus
    
    def get_attack(self) -> int:
        return self._character.get_attack() + self._damage_bonus
    
    def get_description(self) -> str:
        return f"{self._character.get_description()} + Espada (+{self._damage_bonus} ATK)"


class BowDecorator(ItemDecorator):
    """Arco que aumenta ataque y velocidad"""
    
    def __init__(self, character: Character, damage_bonus: int = 10, speed_bonus: int = 5):
        super().__init__(character)
        self._damage_bonus = damage_bonus
        self._speed_bonus = speed_bonus
    
    def get_attack(self) -> int:
        return self._character.get_attack() + self._damage_bonus
    
    def get_speed(self) -> int:
        return self._character.get_speed() + self._speed_bonus
    
    def get_description(self) -> str:
        return (f"{self._character.get_description()} + Arco "
                f"(+{self._damage_bonus} ATK, +{self._speed_bonus} SPD)")


class MagicStaffDecorator(ItemDecorator):
    """Bastón mágico que aumenta mucho el ataque pero reduce velocidad"""
    
    def __init__(self, character: Character, damage_bonus: int = 25, speed_penalty: int = 3):
        super().__init__(character)
        self._damage_bonus = damage_bonus
        self._speed_penalty = speed_penalty
    
    def get_attack(self) -> int:
        return self._character.get_attack() + self._damage_bonus
    
    def get_speed(self) -> int:
        return max(1, self._character.get_speed() - self._speed_penalty)
    
    def get_description(self) -> str:
        return (f"{self._character.get_description()} + Bastón Mágico "
                f"(+{self._damage_bonus} ATK, -{self._speed_penalty} SPD)")
