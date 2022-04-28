class Loot:
    name = ""
    rarity = "USUAL"
    price = 0
    weight = 0

    def __init__(self, name, rarity, price, weight):
        self.name = name
        self.price = price
        self.rarity = rarity
        self.weight = weight


class Medicament(Loot):

    def __init__(self, name, rarity, price, weight,
                 shelf_live_in_hours, hp_change, hunger_change, thirst_change, cheerfulness_change, radiation_change):
        super().__init__(name, rarity, price, weight)
        self.hp_change = hp_change
        self.hunger_change = hunger_change
        self.thirst_change = thirst_change
        self.radiation_change = radiation_change
        self.shelf_live_in_hours = shelf_live_in_hours
        self.cheerfulness_change = cheerfulness_change


class Weapon(Loot):
    damage, durability = 0, 0

    def __init__(self, name, rarity, price, weight,
                 damage, durability):
        super().__init__(name, rarity, price, weight)
        self.damage = damage
        self.durability = durability


class Armor(Loot):

    def __init__(self, name, rarity, price, weight, hp, radiation_resist, body_part, durability):
        super(Armor, self).__init__(name, rarity, price, weight)
        self.hp = hp
        self.radiation_resist = radiation_resist
        self.body_part = body_part
        self.durability = durability


inf = 10e9


class MedicineGenerator:
    name = ""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def generate_bandage():
        return Medicament("Bandage", "USUAL", 5, 0.1, inf, 20, 0, 0, 0, 0)

    @staticmethod
    def generate_first_aid_kit():
        return Medicament("First aid kid", "RARE", 20, 0.5, inf, 50, 0, 0, 10, -30)

    @staticmethod
    def generate_anti_radiation():
        return Medicament("Anti-radiation pills", "RARE", 10, 0.1, inf, 0, 0, 0, 0, -50)

    @staticmethod
    def generate_tea():
        return Medicament("Tea", "USUAL", 5, 0.5, 48, 5, 5, 40, 20, -10)

    @staticmethod
    def generate_coffee():
        return Medicament("Coffee", "USUAL", 5, 0.5, 48, 5, 5, 35, 30, -10)


class WeaponGenerator:
    name = ""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def generate_empty_weapon():
        return Weapon("Your arms", "USUAL", 0, 0, 5, inf)

    @staticmethod
    def generate_knife():
        return Weapon("Knife", "USUAL", 20, 0.3, 20, 20)


class ArmorGenerator:
    name = ""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def generate_empty_body():
        return Armor("Nothing on body", "USUAL", 0, 0, 0, 0, "BODY", inf)

    @staticmethod
    def generate_empty_head():
        return Armor("Nothing on head", "USUAL", 0, 0, 0, 0, "HEAD", inf)

    @staticmethod
    def generate_motorcycle_helmet():
        return Armor("Motorcycle helmet", "RARE", 10, 1, 30, 15, "HEAD", 50)

    @staticmethod
    def generate_motorcycle_jacket():
        return Armor("Motorcycle jacket", "RARE", 10, 1, 80, 15, "BODY", 40)

