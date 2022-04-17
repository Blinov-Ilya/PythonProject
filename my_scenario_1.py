import EventLoop
import MainCharacter
import Mobs
import Locations
import Loot


def true_function(condition):
    return True


def constant_no_args():
    pass


def constant(condition):
    pass


def fight_mob(condition):
    mob = condition.current_mob
    mob_real_damage = mob.damage - condition.current_main_character.head_armor \
                      - condition.current_main_character.body_armor
    hero_real_damage = condition.current_main_character.current_weapon.damage - mob.armor
    main_character_temp = condition.current_main_character
    main_character_temp.hunger -= 5
    main_character_temp.thirst -= 5
    main_character_temp.cheerfulness -= 5
    if hero_real_damage <= 0:
        main_character_temp.hp = 0
        return
    times = ((mob.hp - 1) // hero_real_damage) + 1
    main_character_temp.body_armor.durability -= times
    main_character_temp.head_armor.durability -= times
    main_character_temp.current_weapon.durability -= times
    if main_character_temp.body_armor.durability <= 0:
        main_character_temp.inventory_set.remove(main_character_temp.body_armor)
        main_character_temp.body_armor = Loot.ArmorGenerator.generate_empty_body()
        print("Body armor is over")
    if main_character_temp.head_armor.durability <= 0:
        main_character_temp.inventory_set.remove(main_character_temp.head_armor)
        main_character_temp.head_armor = Loot.ArmorGenerator.generate_empty_head()
        print("Head armor is over")
    if main_character_temp.current_weapon.durability <= 0:
        main_character_temp.inventory_set.remove(main_character_temp.current_weapon)
        main_character_temp.current_weapon = Loot.WeaponGenerator.generate_empty_weapon()
        print("Weapon armor is over")
    if mob_real_damage < 0:
        return
    main_character_temp.hp -= times * mob_real_damage


def use_bandage(condition):
    condition.current_main_character.hp += 20


def use_first_aid_kid(condition):
    condition.current_main_character.hp += 50
    condition.current_main_character.cheerfulness += 10
    condition.current_main_character.radiation -= 30


def change_location_to_desert(condition):
    condition.current_location = Locations.LocationGenerator.generate_desert()


def print_info(condition):
    print("Name: " + str(condition.current_main_character.name))
    print("HP: " + str(condition.current_main_character.hp))
    print("Hunger: " + str(condition.current_main_character.hunger))
    print("Thirst: " + str(condition.current_main_character.thirst))
    print("Cheerfulness: " + str(condition.current_main_character.cheerfulness))
    print("Radiation: " + str(condition.current_main_character.radiation))
    print("Observation: " + str(condition.current_main_character.observation))
    print("Stealthiness: " + str(condition.current_main_character.stealthiness))
    print("Current weapon: " + str(condition.current_main_character.current_weapon.name))
    print("Head armor: " + str(condition.current_main_character.head_armor.name))
    print("Body armor: " + str(condition.current_main_character.body_armor.name))
    print("Current location: " + str(condition.current_location.name))
    print("Current_mob: " + str(condition.current_mob.name))


main_loc = Locations.LocationGenerator.generate_forest()
main_menu_list_of_answers = ["Watch my character", "Choose bandage", "Choose first-aid kid", "Go to the desert"]
main_menu_replica = EventLoop.Replica(0, "Main menu. Watch options: ", true_function, constant, main_menu_list_of_answers,
    [1, 3, 4, 5])
change_location_to_desert_replica = EventLoop.Replica(5, "You are in desert now!", true_function,
    change_location_to_desert, ["Go to main menu"], [0])
last_replica = EventLoop.Replica(6, "You finished the game! Congratulations! Now you can close the program",
                                 true_function, constant,
                                 ["Exit"], [5])
second_replica = EventLoop.Replica(3, "You've chosen bandage", true_function, use_bandage,
    ["To main menu"], [0])
third_replica = EventLoop.Replica(4, "You've chosen first-aid kid", true_function,
    use_first_aid_kid, ["Go to main menu"], [0])
watching_replica = EventLoop.Replica(0, "You are watching your character", true_function, print_info,
                                     ["Go to main menu"], [0])
first_replica = EventLoop.Replica(2, "Choose product to eat or watch your character info", true_function, constant,
                                  ["Choose bandage", "Choose first-aid kid", "Watch my character"],
                                  [3, 4, 1])

list_of_all_replicas = [main_menu_replica, watching_replica, first_replica, second_replica, third_replica, change_location_to_desert_replica, last_replica]
main_data_base = EventLoop.DataBase(list_of_all_replicas)
Petya = MainCharacter.MainCharacter("Petya", 100, 100, 100, 100, 0, set(), 0, 0,
                                    Loot.WeaponGenerator.generate_empty_weapon(),
                                    Loot.ArmorGenerator.generate_empty_head(),
                                    Loot.ArmorGenerator.generate_empty_body())
timer = 0
current_main_character = Petya
current_location = main_loc
current_mob = Mobs.MobGenerator.generate_empty()
replica_to_begin = 1
database = main_data_base
