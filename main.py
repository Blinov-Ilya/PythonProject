import EventLoop
import MainCharacter
import Mobs
import Locations
import Loot


def true_function():
    return True


def constant():
    pass


main_stat_empty_action = EventLoop.MainStatChange(0, 0, 0, 0, 0)
empty_action = EventLoop.Action(constant, main_stat_empty_action, constant, 0, 0, constant, constant, constant)
main_loc = Locations.LocationGenerator.generate_forest()
main_stat_action_bandage = EventLoop.MainStatChange(20, 0, 0, 0, 0)
main_stat_action_first_aid_kid = EventLoop.MainStatChange(50, 0, 0, 10, -30)
action_bandage = EventLoop.Action(main_loc, main_stat_action_bandage, constant, 0, 0, constant, constant, constant)
action_first_aid_kid = EventLoop.Action(main_loc, main_stat_action_first_aid_kid,
                                        constant, 0, 0, constant, constant, constant)
Petya = MainCharacter.MainCharacter("Petya", 100, 100, 100, 100, 0, set(), 0, 0,
                                    Loot.WeaponGenerator.generate_empty_weapon(),
                                    Loot.ArmorGenerator.generate_empty_head(),
                                    Loot.ArmorGenerator.generate_empty_body())
second_replica = EventLoop.Replica("You've chosen bandage", "Choose bandage", true_function, action_bandage, {})
third_replica = EventLoop.Replica("You've chosen first-aid kid", "Choose first-aid kid", true_function,
                                  action_first_aid_kid, {})
first_replica = EventLoop.Replica("Explore current location", "Choose product to eat", true_function, empty_action,
                                  {second_replica, third_replica})
main_event = EventLoop.Event(0, Petya, main_loc, first_replica)
main_event.action()

