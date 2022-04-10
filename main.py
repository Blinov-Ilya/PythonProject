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
    mob_real_damage = mob.damage - condition.current_main_character.head_armor\
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


# main_stat_empty_action = EventLoop.MainStatChange(0, 0, 0, 0, 0)
# empty_action = EventLoop.Action(constant, main_stat_eempty_actionmpty_action, constant, 0, 0, constant, constant, constant)
main_loc = Locations.LocationGenerator.generate_forest()
# main_stat_action_bandage = EventLoop.MainStatChange(20, 0, 0, 0, 0)
# main_stat_action_first_aid_kid = EventLoop.MainStatChange(50, 0, 0, 10, -30)
# action_bandage = EventLoop.Action(main_loc, main_stat_action_bandage, constant, 0, 0, constant, constant, constant)
# action_first_aid_kid = EventLoop.Action(main_loc, main_stat_action_first_aid_kid,
#                                         constant, 0, 0, constant, constant, constant)
Petya = MainCharacter.MainCharacter("Petya", 100, 100, 100, 100, 0, set(), 0, 0,
                                    Loot.WeaponGenerator.generate_empty_weapon(),
                                    Loot.ArmorGenerator.generate_empty_head(),
                                    Loot.ArmorGenerator.generate_empty_body())
second_replica = EventLoop.Replica("Choose bandage", "You've chosen bandage", true_function, use_bandage, [], {})
third_replica = EventLoop.Replica("Choose first-aid kid", "You've chosen first-aid kid", true_function,
                                  use_first_aid_kid, [], {})
watching_replica = EventLoop.Replica("Watch my character", "You are watching your character", true_function, print_info,
    ["Choose bandage", "Choose first-aid kid", "Watch my character"], {hash("Choose bandage"): second_replica,
    hash("Choose first-aid kid"): third_replica})
watching_replica.map_answer_hash_replica[hash("Watch my character")] = watching_replica
first_replica = EventLoop.Replica("Explore current location", "Choose product to eat or watch your character info", true_function, constant,
    ["Choose bandage", "Choose first-aid kid", "Watch my character"], {hash("Choose bandage"): second_replica,
    hash("Choose first-aid kid"): third_replica, hash("Watch my character"): watching_replica})

main_event = EventLoop.Event(0, Petya, main_loc, Mobs.MobGenerator.generate_empty(), [first_replica])
main_event.action()

