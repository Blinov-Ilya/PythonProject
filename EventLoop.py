import MainCharacter
import Mobs
import Loot
import Locations

# recursive function?


class Replica:

    def __init__(self, text_of_choice_before, text, check_if_applicable, main_action, list_of_replicas_next):
        self.text_of_choice_before = text_of_choice_before
        self.text = text
        self.check_if_applicable = check_if_applicable
        self.main_action = main_action
        self.list_of_replicas_next = list_of_replicas_next


class MainStatChange:

    def __init__(self, hp_change, hunger_change, thirst_change, cheerfulness_change, radiation_change):
        self.hp_change = hp_change
        self.hunger_change = hunger_change
        self.thirst_change = thirst_change
        self.cheerfulness_change = cheerfulness_change
        self.radiation_change = radiation_change


class Action:
    # inventory_set_change is a function, head_armor_change is a function, new_location is a function
    def __init__(self, new_location, main_stat_change, inventory_set_change, observation_change, stealthiness_change,
                 current_weapon_change, head_armor_change, body_armor_change):
        self.new_location = new_location
        self.main_stat_change = main_stat_change
        self.inventory_set_change = inventory_set_change
        self.observation_change = observation_change
        self.stealthiness_change = stealthiness_change
        self.current_weapon_change = current_weapon_change
        self.head_armor_change = head_armor_change
        self.body_armor_change = body_armor_change


class Event:

    timer, current_main_character, current_location = 0, MainCharacter.MainCharacter("", 0, 0, 0, 0, 0, set(), 0, 0,
        Loot.WeaponGenerator.generate_knife(), Loot.ArmorGenerator.generate_motorcycle_helmet(),
        Loot.ArmorGenerator.generate_motorcycle_jacket()), Locations.LocationGenerator.generate_forest()

    def __init__(self, timer, current_main_character, current_location, current_replica):
        self.timer = timer
        self.current_main_character = current_main_character
        self.current_location = current_location
        self.current_replica = current_replica

    def fight_mob(self, mob):
        mob_real_damage = mob.damage - self.current_main_character.head_armor - self.current_main_character.body_armor
        hero_real_damage = self.current_main_character.current_weapon.damage - mob.armor
        self.current_main_character.hunger -= 5
        self.current_main_character.thirst -= 5
        self.current_main_character.cheerfulness -= 5
        if hero_real_damage <= 0:
            self.current_main_character.hp = 0
            return
        times = ((mob.hp - 1) // hero_real_damage) + 1
        self.current_main_character.body_armor.durability -= times
        self.current_main_character.head_armor.durability -= times
        self.current_main_character.current_weapon.durability -= times
        if self.current_main_character.body_armor.durability <= 0:
            self.current_main_character.inventory_set.remove(self.current_main_character.body_armor)
            self.current_main_character.body_armor = Loot.ArmorGenerator.generate_empty_body()
            print("Body armor is over")
        if self.current_main_character.head_armor.durability <= 0:
            self.current_main_character.inventory_set.remove(self.current_main_character.head_armor)
            self.current_main_character.head_armor = Loot.ArmorGenerator.generate_empty_head()
            print("Head armor is over")
        if self.current_main_character.current_weapon.durability <= 0:
            self.current_main_character.inventory_set.remove(self.current_main_character.current_weapon)
            self.current_main_character.current_weapon = Loot.WeaponGenerator.generate_empty_weapon()
            print("Weapon armor is over")
        if mob_real_damage < 0:
            return
        self.current_main_character.hp -= times * mob_real_damage

    def action(self):
    # no need if self.current_replica.check_if_applicable due to we've already checked it before in the end of the previous action
        print(self.current_replica.text)
        if self.current_replica.text_of_choice_before == "Explore current location":
            self.current_main_character.inventory_set.update(self.current_location.explore())
            self.current_main_character.hunger -= 5
            self.current_main_character.thirst -= 5
            self.current_main_character.cheerfulness -= 5
            self.current_main_character.radiation += self.current_location.radiation_per_time
            self.timer += 1
            list_of_replicas_possible = list()
            for replica in self.current_replica.list_of_replicas_next:
                if replica.check_if_applicable():
                    print(replica.text)
                    list_of_replicas_possible.append(replica)
            index = int(input()) - 1
            self.current_replica = list_of_replicas_possible[index]
            return self.action()
        act = self.current_replica.main_action

        # TODO: loot from monsters, location, explore location
        self.timer += 1
    # each possibility has it's action in dict and variants of next possibilities

