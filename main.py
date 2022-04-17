import EventLoop
import MainCharacter
import Mobs
import Locations
import Loot
import sys
import FileHandler


# last_replica = EventLoop.Replica("")
path = sys.argv[1]
file_handler = FileHandler.FileHandler(path)
main_event = EventLoop.Event(file_handler.timer, file_handler.current_main_character, file_handler.current_location,
                             file_handler.current_mob, file_handler.replica_to_begin, file_handler.database)
main_event.action()

