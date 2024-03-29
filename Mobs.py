from Loot import MedicineGenerator


class Mob:

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
        return Mob("No mobs nearby", 0, 0, 0, 0, False, {}, 0)

    @staticmethod
    def generate_zombie():
        return Mob("Zombie", 80, 15, 15, 10, False,
                   {hash(MedicineGenerator.generate_bandage().name): 0.15,
                    hash(MedicineGenerator.generate_anti_radiation().name): 0.05}, 3)

