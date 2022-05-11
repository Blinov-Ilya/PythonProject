import EventLoop
import sys
import FileHandler
import app

app.app.run("0.0.0.0", 5000)
path = sys.argv[1]
file_handler = FileHandler.FileHandler(path)
main_event = EventLoop.Event(file_handler.timer, file_handler.current_main_character, file_handler.current_location,
                             file_handler.current_mob, file_handler.replica_to_begin, file_handler.database)
main_event.action()

