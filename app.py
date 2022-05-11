from flask import Flask, render_template, request, url_for, redirect, flash
import EventLoop
import FileHandler

app = Flask(__name__)
app.secret_key = 'some very secret key'

scenario_list = list()  # scenarios list, to each number we have a path to corresponding scenario
scenario_list.append('/home/ilya/PycharmProjects/QuestProject/my_scenario_1.py')


# scenario_list.append('try anything else)')
main_event = None
list_of_replicas_possible = list()
answer_strings = list()


@app.route('/', methods=['GET', 'POST'])
def start_page():
    if request.method == 'POST':
        if 'show_scenarios' in request.form:
            # flash("You've chosen 1 button")
            return redirect(url_for('show_scenarios'))
        if 'run_chosen_scenario' in request.form:
            scenario_number = int(request.form['scenario']) - 1
            print(scenario_number)
            path = scenario_list[scenario_number]
            file_handler = FileHandler.FileHandler(path)
            global main_event
            main_event = EventLoop.Event(file_handler.timer, file_handler.current_main_character,
                                         file_handler.current_location,
                                         file_handler.current_mob, file_handler.replica_to_begin, file_handler.database)
            return redirect(url_for('start_scenario'))
        if 'ToMainPage' in request.form:
            return redirect("http://localhost:5000/")
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template("index.html")


# on start page we upload scenario or choose one from the followings


@app.route('/show_var/<to_show>')
def show_var(to_show=None):
    return render_template('show_var.html', var=to_show)


@app.route('/shown_scenarios', methods=['GET', 'POST'])
def show_scenarios():
    if request.method == 'POST':
        if 'To main page' in request.form:
            return redirect("http://localhost:5000/")
    return render_template("with_scenarios.html", list_of_scenarios=scenario_list)


@app.route('/process_scenario/starter', methods=['GET', 'POST'])
def start_scenario():
    global main_event
    global answer_strings
    global list_of_replicas_possible
    current_replica = main_event.database.list_of_replicas[main_event.condition.current_replica_id]
    # print("Options: ")
    answer_strings = [current_replica.text, "Options: "]
    counter = 0
    for answer in current_replica.list_of_answers:
        helper = current_replica.map_answer_hash_replica_id[hash(answer)]
        if main_event.database.list_of_replicas[helper].check_if_applicable(main_event.condition):
            counter += 1
            # print(str(counter) + ": " + answer)
            answer_strings.append(str(counter) + ": " + answer)
            list_of_replicas_possible.append(current_replica.map_answer_hash_replica_id[hash(answer)])
    # print("\nChoose the option by it's number in list beginning from 1")
    answer_strings.append("")
    answer_strings.append("Choose the option by it's number in list beginning from 1")
    return redirect(url_for('process_scenario'))


@app.route('/process_scenario', methods=['GET', 'POST'])
def process_scenario():
    # number_of_scenario = int(number_of_scenario)
    # path = scenario_list[number_of_scenario]
    # file_handler = FileHandler.FileHandler(path)
    global main_event
    global answer_strings
    global list_of_replicas_possible
    if request.method == 'POST':
        if 'send_answer' in request.form:
            index = 0
            flag = True
            while flag:
                input_string = request.form["client_answer"]
                try:
                    index = int(input_string) - 1
                    if index >= len(list_of_replicas_possible) or index < 0:
                        raise ValueError
                    main_event.condition.current_replica_id = list_of_replicas_possible[index]
                    lis = get_replicas(main_event)
                    list_of_replicas_possible = lis[0]
                    answer_strings = lis[1]
                    flag = False
                except ValueError:
                    return render_template("run_scenario.html", list_of_answers=
                    ["Oops!  That was not valid number.  Try again...(enter 1 to get to main menu)"], person_info=get_info(main_event.condition))
            return render_template("run_scenario.html", list_of_answers=answer_strings, person_info=get_info(main_event.condition))
        if 'to_main_page' in request.form:
            return redirect("http://localhost:5000/")
    elif request.method == 'GET':
        return render_template('run_scenario.html', list_of_answers=answer_strings, person_info=get_info(main_event.condition))
    return render_template("run_scenario.html", list_of_answers=answer_strings, person_info=get_info(main_event.condition))


def get_info(condition):
    strings = ["Name: " + str(condition.current_main_character.name),
                      "HP: " + str(condition.current_main_character.hp),
                      "Hunger: " + str(condition.current_main_character.hunger),
                      "Thirst: " + str(condition.current_main_character.thirst),
                      "Cheerfulness: " + str(condition.current_main_character.cheerfulness),
                      "Radiation: " + str(condition.current_main_character.radiation),
                      "Observation: " + str(condition.current_main_character.observation),
                      "Stealthiness: " + str(condition.current_main_character.stealthiness),
                      "Current weapon: " + str(condition.current_main_character.current_weapon.name),
                      "Head armor: " + str(condition.current_main_character.head_armor.name),
                      "Body armor: " + str(condition.current_main_character.body_armor.name),
                      "Current location: " + str(condition.current_location.name),
                      "Current_mob: " + str(condition.current_mob.name)]
    return strings


def get_replicas(current_event):  # returns options, output
    current_replica = current_event.database.list_of_replicas[current_event.condition.current_replica_id]
    # print(current_replica.text)
    current_replica.main_action(current_event.condition)
    list_of_replicas_possible = list()
    # print("Options: ")
    answer_strings = [current_replica.text, "Options: "]
    counter = 0
    for answer in current_replica.list_of_answers:
        helper = current_replica.map_answer_hash_replica_id[hash(answer)]
        if current_event.database.list_of_replicas[helper].check_if_applicable(current_event.condition):
            counter += 1
            # print(str(counter) + ": " + answer)
            answer_strings.append(str(counter) + ": " + answer)
            list_of_replicas_possible.append(current_replica.map_answer_hash_replica_id[hash(answer)])
    # print("\nChoose the option by it's number in list beginning from 1")
    answer_strings.append("")
    answer_strings.append("Choose the option by it's number in list beginning from 1")
    to_return = [list_of_replicas_possible, answer_strings]
    return to_return


app.run("0.0.0.0", 5000)
