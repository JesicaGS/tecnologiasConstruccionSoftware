from character import Character

class BaseCharacter(Character):
    """Personaje base sin items equipados"""
    
    def __init__(self, name: str, base_attack: int = 10, 
                 base_defense: int = 5, base_speed: int = 8):
        self.name = name
        self._base_attack = base_attack
        self._base_defense = base_defense
        self._base_speed = base_speed
    
    def get_attack(self) -> int:
        return self._base_attack
    
    def get_defense(self) -> int:
        return self._base_defense
    
    def get_speed(self) -> int:
        return self._base_speed
    
    def get_description(self) -> str:
        return f"{self.name} (Sin equipamiento)"

