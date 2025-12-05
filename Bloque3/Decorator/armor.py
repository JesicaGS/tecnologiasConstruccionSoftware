from item_decorator import ItemDecorator
from character import Character

class LeatherArmorDecorator(ItemDecorator):
    """Armadura de cuero ligera"""
    
    def __init__(self, character: Character, defense_bonus: int = 8):
        super().__init__(character)
        self._defense_bonus = defense_bonus
    
    def get_defense(self) -> int:
        return self._character.get_defense() + self._defense_bonus
    
    def get_description(self) -> str:
        return f"{self._character.get_description()} + Armadura de Cuero (+{self._defense_bonus} DEF)"


class IronArmorDecorator(ItemDecorator):
    """Armadura de hierro pesada"""
    
    def __init__(self, character: Character, defense_bonus: int = 20, speed_penalty: int = 4):
        super().__init__(character)
        self._defense_bonus = defense_bonus
        self._speed_penalty = speed_penalty
    
    def get_defense(self) -> int:
        return self._character.get_defense() + self._defense_bonus
    
    def get_speed(self) -> int:
        return max(1, self._character.get_speed() - self._speed_penalty)
    
    def get_description(self) -> str:
        return (f"{self._character.get_description()} + Armadura de Hierro "
                f"(+{self._defense_bonus} DEF, -{self._speed_penalty} SPD)")


class MysticRobeDecorator(ItemDecorator):
    """Túnica mística que da defensa y velocidad"""
    
    def __init__(self, character: Character, defense_bonus: int = 10, speed_bonus: int = 3):
        super().__init__(character)
        self._defense_bonus = defense_bonus
        self._speed_bonus = speed_bonus
    
    def get_defense(self) -> int:
        return self._character.get_defense() + self._defense_bonus
    
    def get_speed(self) -> int:
        return self._character.get_speed() + self._speed_bonus
    
    def get_description(self) -> str:
        return (f"{self._character.get_description()} + Túnica Mística "
                f"(+{self._defense_bonus} DEF, +{self._speed_bonus} SPD)")
