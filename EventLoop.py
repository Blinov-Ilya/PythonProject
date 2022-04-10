import MainCharacter
import Mobs
import Loot
import Locations


# recursive function?


class Replica:  # replica determines by the text_of_choice_before?
    # main_action is a function of changes takes the current condition

    def __init__(self, text_of_choice_before, text, check_if_applicable, main_action, list_of_answers,
                 map_answer_hash_replica):
        self.text_of_choice_before = text_of_choice_before
        self.text = text
        self.check_if_applicable = check_if_applicable
        self.main_action = main_action
        self.list_of_answers = list_of_answers
        self.map_answer_hash_replica = map_answer_hash_replica


# class MainStatChange:
#
#     def __init__(self, hp_change, hunger_change, thirst_change, cheerfulness_change, radiation_change):
#         self.hp_change = hp_change
#         self.hunger_change = hunger_change
#         self.thirst_change = thirst_change
#         self.cheerfulness_change = cheerfulness_change
#         self.radiation_change = radiation_change
#
#
# class Action:
#     # inventory_set_change is a function, head_armor_change is a function, new_location is a function
#     def __init__(self, change_function):
#         self.function_of_changes = change_function
#

class Condition:
    
    def __init__(self, timer, current_main_character, current_location, current_mob, list_of_replicas):
        self.timer = timer
        self.current_main_character = current_main_character
        self.current_location = current_location
        self.current_mob = current_mob
        self.list_of_replicas = list_of_replicas


class Event:
    condition = Condition(0, MainCharacter.MainCharacter("", 0, 0, 0, 0, 0,
        set(), 0, 0,
        Loot.WeaponGenerator.generate_knife(),
        Loot.ArmorGenerator.generate_motorcycle_helmet(),
        Loot.ArmorGenerator.generate_motorcycle_jacket()), Locations.LocationGenerator.generate_forest(), \
        Mobs.MobGenerator.generate_empty(), list())

    def __init__(self, timer, current_main_character, current_location, current_mob, list_of_replicas):
        self.condition = Condition(timer, current_main_character, current_location, current_mob, list_of_replicas)

    def action(self):
        # no need if current_replica.check_if_applicable due to we've already checked
        # it before in the end of the previous action
        current_replica = self.condition.list_of_replicas[-1]
        main_character_temp = self.condition.current_main_character
        print(current_replica.text)
        # comment all below due to we've got the function in replica
        # if current_replica.text_of_choice_before == "Explore current location":
        #     main_character_temp.inventory_set.update(self.condition.current_location.explore())
        #     main_character_temp.hunger -= 5
        #     main_character_temp.thirst -= 5
        #     main_character_temp.cheerfulness -= 5
        #     main_character_temp.radiation += self.condition.current_location.radiation_per_time
        #     self.condition.timer += 1
        #     list_of_replicas_possible = list()
        #     for replica in current_replica.list_of_replicas_next:
        #         if replica.check_if_applicable():
        #             print(replica.text)
        #             list_of_replicas_possible.append(replica)
        #     index = int(input()) - 1
        #     current_replica = list_of_replicas_possible[index]
        #     return self.action()
        # self, text_of_choice_before, text, check_if_applicable, main_action, list_of_answers,
        #                  map_answer_hash_replica
        current_replica.main_action(self.condition)
        list_of_replicas_possible = list()
        print("Options: ")
        counter = 0
        for answer in current_replica.list_of_answers:
            if current_replica.map_answer_hash_replica[hash(answer)].check_if_applicable(self.condition):
                counter += 1
                print(str(counter) + ": " + answer)
                list_of_replicas_possible.append(current_replica.map_answer_hash_replica[hash(answer)])
        print("\nChoose the option by it's number in list beginning from 1")
        index = int(input()) - 1
        self.condition.list_of_replicas.append(list_of_replicas_possible[index])
        return self.action()
        # TODO: loot from monsters, location, explore location
    # each possibility has it's action in dict and variants of next possibilities
