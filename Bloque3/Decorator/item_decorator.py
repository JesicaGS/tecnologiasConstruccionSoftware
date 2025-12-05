from character import Character

class ItemDecorator(Character):
    """Decorador base para items del personaje"""
    
    def __init__(self, character: Character):
        self._character = character
    
    def get_attack(self) -> int:
        return self._character.get_attack()
    
    def get_defense(self) -> int:
        return self._character.get_defense()
    
    def get_speed(self) -> int:
        return self._character.get_speed()
    
    def get_description(self) -> str:
        return self._character.get_description()
