from Loot import MedicineGenerator
from Loot import ArmorGenerator
from Loot import WeaponGenerator


class MainCharacter:

    def __init__(self, name, hp, hunger, thirst, cheerfulness, radiation, inventory_set,
                 observation, stealthiness, current_weapon, head_armor, body_armor):
        self.name = name
        self.hp = hp
        self.hunger = hunger
        self.thirst = thirst
        self.cheerfulness = cheerfulness
        self.radiation = radiation
        self.inventory_set = inventory_set
        self.observation = observation
        self.stealthiness = stealthiness
        self.current_weapon = current_weapon
        self.head_armor = head_armor
        self.body_armor = body_armor

