from Loot import MedicineGenerator


class Mob:
    name, hp, damage, observation, stealthiness, is_talkative, map_loot_hash_possibility, armor = "",\
        0, 0, 0, 0, False, dict(), 0

    def __init__(self, name, hp, damage, observation, stealthiness, is_talkative, map_loot_hash_poss, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.observation = observation
        self.stealthiness = stealthiness
        self.is_talkative = is_talkative
        self.map_loot_hash_possibility = map_loot_hash_poss
        self.armor = armor


class MobGenerator:
    name = ""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def generate_empty():
        return Mob("Empty mob", 0, 0, 0, 0, False, {}, 0)

    @staticmethod
    def generate_zombie():
        return Mob("Zombie", 80, 15, 15, 10, False,
                   {MedicineGenerator.generate_bandage().__hash__(): 0.15,
                    MedicineGenerator.generate_anti_radiation().__hash__(): 0.05}, 3)

