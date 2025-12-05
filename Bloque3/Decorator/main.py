from base_character import BaseCharacter
from weapons import SwordDecorator, BowDecorator, MagicStaffDecorator
from armor import LeatherArmorDecorator, IronArmorDecorator, MysticRobeDecorator
from accessories import BootsOfSpeedDecorator, ShieldDecorator, RingOfPowerDecorator

def print_character_stats(character):
    """Muestra las estadísticas del personaje"""
    print("\n" + "="*60)
    print(character.get_description())
    print("-"*60)
    print(f"ATK: {character.get_attack()}")
    print(f"DEF: {character.get_defense()}")
    print(f"SPD: {character.get_speed()}")
    print("="*60)

def main():

    # Ejemplo 2: Guerrero pesado
    print("\n\n GUERRERO PESADO ")
    warrior = BaseCharacter("Guerrero", base_attack=15, base_defense=10, base_speed=5)
    warrior = SwordDecorator(warrior, damage_bonus=20)
    warrior = IronArmorDecorator(warrior, defense_bonus=20, speed_penalty=4)
    warrior = ShieldDecorator(warrior, defense_bonus=12, speed_penalty=2)
    print_character_stats(warrior)
    
    # Ejemplo 3: Arquero ágil
    print("\n\n ARQUERO ÁGIL ")
    archer = BaseCharacter("Arquero", base_attack=12, base_defense=3, base_speed=12)
    archer = BowDecorator(archer, damage_bonus=10, speed_bonus=5)
    archer = LeatherArmorDecorator(archer, defense_bonus=8)
    archer = BootsOfSpeedDecorator(archer, speed_bonus=10)
    print_character_stats(archer)
    
    # Ejemplo 4: Mago poderoso
    print("\n\n MAGO PODEROSO ")
    mage = BaseCharacter("Mago", base_attack=8, base_defense=4, base_speed=7)
    mage = MagicStaffDecorator(mage, damage_bonus=25, speed_penalty=3)
    mage = MysticRobeDecorator(mage, defense_bonus=10, speed_bonus=3)
    mage = RingOfPowerDecorator(mage, all_stats_bonus=5)
    print_character_stats(mage)
    

if __name__ == "__main__":
    main()
