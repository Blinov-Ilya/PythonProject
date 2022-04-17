from Mobs import MobGenerator
from Loot import MedicineGenerator
from random import randint


class Location:
    def __init__(self, name, radiation_per_time, map_mob_name_hash_possibility, map_loot_hash_possibility):
        self.name = name
        self.radiation_per_time = radiation_per_time
        self.map_mob_name_hash_possibility = map_mob_name_hash_possibility
        self.map_loot_hash_possibility = map_loot_hash_possibility

    def mobs_attack(self):
        for mob in self.map_mob_name_hash_possibility.keys():
            if randint(1, 10000) <= self.map_mob_name_hash_possibility[mob] * 10000:
                return mob
        return MobGenerator.generate_empty()

    def explore(self):
        set_of_loot = set()
        for loot in self.map_loot_hash_possibility.keys():
            if randint(1, 10000) <= self.map_mob_name_hash_possibility[loot] * 10000:
                set_of_loot.add(loot)
        return set_of_loot


class LocationGenerator:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def generate_forest():
        return Location("Forest", 0, {hash(MobGenerator.generate_zombie().name): 0.1},
                        {hash(MedicineGenerator.generate_bandage().name): 0.01})

    @staticmethod
    def generate_desert():
        return Location("Desert", 1, {hash(MobGenerator.generate_zombie().name): 0.01}, {})
