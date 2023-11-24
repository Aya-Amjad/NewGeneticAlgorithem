import matplotlib.pyplot as plt
import numpy as np
import prettytable

from GeneticAlgorithm import NUMBER_OF_ELITE_LECTURES, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, POPULATION_SIZE


def print_courses(courses):
    courses_table = prettytable.PrettyTable(['id of course', 'course', 'Doctors'])
    for course in courses:
        docents = course.get_docents()
        temp_str = ""
        for i, docent in enumerate(docents):
            temp_str += str(docent)
            if i < len(docents) - 1:
                temp_str += " | "
        courses_table.add_row([course.get_number(), course.get_name(), temp_str])
    print(courses_table)



def print_docents(instructors):
    available_docents_table = prettytable.PrettyTable(['id of doctor', 'Doctor'])
    for i in range(0, len(instructors)):
        available_docents_table.add_row([instructors[i].get_id(), instructors[i].get_name()])
    print(available_docents_table)



def print_meeting_times(meeting_times):
    available_meeting_time_table = prettytable.PrettyTable(['Slot', 'Day', 'Time'])
    for i in range(0, len(meeting_times)):
        available_meeting_time_table.add_row([meeting_times[i].get_id(), meeting_times[i].get_days(), meeting_times[i].get_time()])
    print(available_meeting_time_table)


def print_generation(schedules):
    generation_table = prettytable.PrettyTable(
        ['#', 'Fitness', 'Anzahl Konflikte', 'Vorlesung [Modul, Raum, Dozent, Zeitraum]'])

    for i in range(0, len(schedules)):
        classes = schedules[i].get_lectures()
        lecture_info = ""
        for j in range(0, len(classes)):
            lecture_info += classes[j].get_course().get_name() + " (" + str(classes[j].get_course().get_number_of_students()) + ")"
            lecture_info += ", " + classes[j].get_room().get_number() + " (" + str(classes[j].get_room().get_seating_capacity()) + ")"
            lecture_info += ", " + classes[j].get_docent().get_name() + " (" + str(classes[j].get_docent().get_id()) + ")"
            lecture_info += ", " + classes[j].get_meeting_time().get_time() + " (" + str(classes[j].get_meeting_time().get_id()) + ")"
            if j < len(classes) - 1:
                lecture_info += " | "
        generation_table.add_row([str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_number_of_conflicts(), lecture_info])
    print(generation_table)


def print_room(rooms):
    available_rooms_table = prettytable.PrettyTable(['Room number', 'capacity'])
    for i in range(0, len(rooms)):
        available_rooms_table.add_row([str(rooms[i].get_number()), str(rooms[i].get_seating_capacity())])
    print(available_rooms_table)



def print_schedule_as_table(schedule):
    classes = schedule.get_lectures()
    table = prettytable.PrettyTable(
        ['Stunde #', 'course', 'room_number(capacity)', 'Doctor','Time Slot (Slot)', 'Day'])
    for i in range(0, len(classes)):
        table.add_row([
            str(i),
            classes[i].get_course().get_name() + " (" +
            str(classes[i].get_course().get_number_of_students()) + ")",

            classes[i].get_room().get_number() + " (" + str(
                classes[i].get_room().get_seating_capacity()) + ")",

            classes[i].get_docent().get_name() + " (" + str(
                classes[i].get_docent().get_id()) + ")",

            classes[i].get_meeting_time().get_time() + " (" + str(
                classes[i].get_meeting_time().get_id()) + ")",
              classes[i].get_meeting_time().get_days() ])
    print(table)


def print_current_population(population, generation_number):
    print("\n> Generation # " + str(generation_number))
    print_generation(population.get_schedules())
    print_schedule_as_table(population.get_schedules()[0])


def plot_diagram(conflicts):
    plt.plot(conflicts)
    plt.ylabel("Anzahl der Konflikte")
    plt.yticks(np.arange(0, conflicts[0] + 1, step=1))
    plt.xlabel("Generationen")
    plt.Text("NUMBER_OF_ELITE_LECTURES: " + str(NUMBER_OF_ELITE_LECTURES))
    plt.Text("TOURNAMENT_SELECTION_SIZE: " + str(TOURNAMENT_SELECTION_SIZE))
    plt.Text("MUTATION_RATE: " + str(MUTATION_RATE))
    plt.Text("POPULATION_SIZE: " + str(POPULATION_SIZE))
    plt.show()


def print_stats(generation_number, conflicts, data):
    print("\n")
    print("Benötigte Generationen: " + str(generation_number))
    print("--")
    print("Verwendete Eingaben:")
    print("Anzahl der Dozenten: " + str(len(data.get_docents())))
    print("Anzahl der Zeitslots: " + str(len(data.get_meeting_times())))
    print("Anzahl der course: " + str(len(data.get_courses())))
    print("--")
    print("Parameter für den genetischen Algorithmus:")
    print("NUMBER_OF_ELITE_LECTURES: " + str(NUMBER_OF_ELITE_LECTURES))
    print("TOURNAMENT_SELECTION_SIZE: " + str(TOURNAMENT_SELECTION_SIZE))
    print("MUTATION_RATE: " + str(MUTATION_RATE))
    print("POPULATION_SIZE: " + str(POPULATION_SIZE))
    print(conflicts)
    print("--")
    #plot_diagram(conflicts)


def print_available_data(data):
    print_courses(data.get_courses())
    print_docents(data.get_docents())
    print_room(data.get_rooms())
    print_meeting_times(data.get_meeting_times())