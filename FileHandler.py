import EventLoop
import MainCharacter
import Mobs
import Locations
import Loot
import importlib
import sys
from importlib.machinery import SourceFileLoader

# file format:
# First - loot
# Loot: type: non, Medicament, Weapon, Armor
# Then arguments according to their constructor
# Second - mobs
# Mobe: arguments according to their constructor
# Third - locations
# Location: name, RPT,  MapMobPoss: <name> : <possibility>, ..., MapLootPoss: <name> : <possibility>
# Forth - MainCharacter
# MC: arguments according to their constructor
# Fifth - database of replicas
# Replica: id, begin_of_text <text> end_of_text, condition: true, MainCharacter.hp > < == 8,
# <condition(stats, name of location, name_of_mob, curr_repl)>,
# Sixth - event


class FileHandler:
    def __init__(self, path_to_module):
        # if path_to_module[-3:] != ".py":
        #     print("not correct path, should be ended by .py")
        # else:
        module_name = ""
        current_symb = 0
        while path_to_module[len(path_to_module) - 1 - current_symb] != "/":
            module_name = path_to_module[len(path_to_module) - 1 - current_symb] + module_name
            current_symb += 1
        sys.path.append(path_to_module[:len(path_to_module) - 1 - current_symb])
        scenario = SourceFileLoader(module_name, path_to_module).load_module()
        self.timer = scenario.timer
        self.current_main_character = scenario.current_main_character
        self.current_location = scenario.current_location
        self.current_mob = scenario.current_mob
        self.database = scenario.database
        self.replica_to_begin = scenario.replica_to_begin

    # file format:
    #