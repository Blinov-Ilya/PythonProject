import MainCharacter
import Mobs
import Loot
import Locations


class Replica:
    # main action is a function
    def __init__(self, id_in_database, text, check_if_applicable, main_action, list_of_answers,
                 list_ids_of_answers_in_the_same_order):
        self.id_in_database = id_in_database
        self.text = text
        self.check_if_applicable = check_if_applicable
        self.main_action = main_action
        self.list_of_answers = list_of_answers
        self.map_answer_hash_replica_id = dict()
        for i in range(len(list_of_answers)):
            self.map_answer_hash_replica_id[hash(list_of_answers[i])] = list_ids_of_answers_in_the_same_order[i]


class DataBase:
    def __init__(self, list_of_replicas):
        self.list_of_replicas = list_of_replicas


class Condition:

    def __init__(self, timer, current_main_character, current_location, current_mob, current_replica_id):
        self.timer = timer
        self.current_main_character = current_main_character
        self.current_location = current_location
        self.current_mob = current_mob
        self.current_replica_id = current_replica_id


class Event:
    database = DataBase(list())
    condition = Condition(0, MainCharacter.MainCharacter("", 0, 0, 0, 0, 0,
        set(), 0, 0,
        Loot.WeaponGenerator.generate_knife(),
        Loot.ArmorGenerator.generate_motorcycle_helmet(),
        Loot.ArmorGenerator.generate_motorcycle_jacket()), Locations.LocationGenerator.generate_forest(), \
        Mobs.MobGenerator.generate_empty(), list())

    def __init__(self, timer, current_main_character, current_location, current_mob, replica_to_begin, database):
        self.condition = Condition(timer, current_main_character, current_location, current_mob, replica_to_begin)
        self.database = database

    def action(self):
        # no need if current_replica.check_if_applicable due to we've already checked
        # it before in the end of the previous action
        current_replica = self.database.list_of_replicas[self.condition.current_replica_id]
        main_character_temp = self.condition.current_main_character
        print(current_replica.text)
        current_replica.main_action(self.condition)
        list_of_replicas_possible = list()
        print("Options: ")
        counter = 0
        for answer in current_replica.list_of_answers:
            helper = current_replica.map_answer_hash_replica_id[hash(answer)]
            if self.database.list_of_replicas[helper].check_if_applicable(self.condition):
                counter += 1
                print(str(counter) + ": " + answer)
                list_of_replicas_possible.append(current_replica.map_answer_hash_replica_id[hash(answer)])
        print("\nChoose the option by it's number in list beginning from 1")
        index = int(input()) - 1
        if index >= len(list_of_replicas_possible) or index < 0:
            print("wrong index!")
        else:
            self.condition.current_replica_id = list_of_replicas_possible[index]
        return self.action()
        # TODO: loot from monsters, location, explore location
    # each possibility has it's action in dict and variants of next possibilities
