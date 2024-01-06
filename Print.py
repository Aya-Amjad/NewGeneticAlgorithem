import matplotlib.pyplot as plt
import numpy as np
import prettytable
from prettytable import PrettyTable
from constants import TIMES
from GeneticAlgorithm import NUMBER_OF_ELITE_LECTURES, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, POPULATION_SIZE
'''
professors = ", ".join([str(professor) for professor in course.professors])
'''

def print_courses(courses):
    courses_table = prettytable.PrettyTable(['code', 'name','#students','#hours','#students/room','requires_projector', 'professors'])
    for course in courses:
        professors = ", ".join([str(professor) for professor in course.professors])
        courses_table.add_row([course.get_number(), course.get_name(), course.get_number_of_students(),course.get_number_of_hours(),course.get_max_students_per_room(),course.get_requires_projector(),professors])
    print(courses_table)

def print_docents(docents):
    docents_table = prettytable.PrettyTable(['ID', 'ID Number', 'Name', 'Min Hours', 'Max Hours'])
    for docent in docents:
        row_data = [
            getattr(docent, attr, 'N/A')  # Use 'N/A' if attribute doesn't exist
            for attr in ['id', 'id_number', 'name', 'min_hours', 'max_hours']
        ]
        docents_table.add_row(row_data)
    print(docents_table)


def print_meeting_times(meeting_times):
    available_meeting_time_table = PrettyTable(['ID', 'Days', 'Time'])
    for meeting_time in meeting_times:
        available_meeting_time_table.add_row([meeting_time[0], meeting_time[1], f"{meeting_time[2]} - {meeting_time[3]}"])
    print(available_meeting_time_table)

def print_generation(schedules):
    generation_table = prettytable.PrettyTable(
        ['#', 'Fitness', 'Anzahl Konflikte', 'Vorlesung [Modul, Raum, Dozent, Zeitraum]'])

    for i in range(0, len(schedules)):
        classes = schedules[i].get_lectures()
        lecture_info = ""

        for j in range(0, len(classes)):

            lecture_info += ", " + classes[j].get_course().get_name() + " (" + str(
                classes[j].get_course().get_number_of_students()) + ")"
            professors_info = ", ".join([professor.name for professor in classes[j].get_course().get_docents()])
            lecture_info += f" {professors_info}"
            lecture_info += ", " + classes[j].get_room().get_number() + " (" + str(
                classes[j].get_room().get_seating_capacity()) + ")"

            # Assuming get_meeting_time() returns a list
            meeting_times = classes[j].get_meeting_time()

            # Handling the case where meeting_times is not empty
            if meeting_times:
                # Ensure each tuple has at least four elements before accessing them
                time_info_str = ", ".join([f"{info[1]} ({info[2]} - {info[3]}) ({info[0]})" for info in TIMES if info[0] == meeting_times[0]])
                lecture_info += ", " + time_info_str

            if j < len(classes) - 1:
                lecture_info += " | "

        generation_table.add_row([str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_number_of_conflicts(), lecture_info])
    print(generation_table)


def print_room(rooms):
    available_rooms_table = prettytable.PrettyTable(['Room number', 'capacity','Room type','Has projector'])
    for i in range(0, len(rooms)):
        available_rooms_table.add_row([str(rooms[i].get_number()), str(rooms[i].get_seating_capacity()),str(rooms[i].get_room_type()),str(rooms[i].get_has_projector())])
    print(available_rooms_table)

def print_schedule_as_table(schedule, meeting_times):
    classes = schedule.get_lectures()
    table = prettytable.PrettyTable(
        ['Stunde #', 'course', 'room_number(capacity)', 'Doctor', 'Time Slot (Slot)', 'Day'])

    for i in range(len(classes)):
        lecture = classes[i]
        meeting_times = lecture.get_meeting_time()

        # Add these prints to identify the issue
        print("Meeting Times:", meeting_times)
        for meeting_time_id in meeting_times:
            print("Meeting Time ID:", meeting_time_id)
            time_info = [info for info in TIMES if info[0] == meeting_time_id]
            print("Time Info:", time_info)

            if time_info:  # Check if time_info is not empty
                time_info = time_info[0]
                table.add_row([
                    str(i),
                    lecture.get_course().get_name() + " (" +
                    str(lecture.get_course().get_number_of_students()) + ")",

                    lecture.get_room().get_number() + " (" + str(
                        lecture.get_room().get_seating_capacity()) + ")",

                    lecture.get_docent().get_name() + " (" + str(
                        lecture.get_docent().get_id()) + ")",

                    f"{time_info[2]} - {time_info[3]} ({meeting_time_id})",
                    ", ".join(time_info[1])
                ])
            else:
                print("No matching time info found for ID:", meeting_time_id)

    print(table)




def print_current_population(population, generation_number):
    print("\n> Generation # " + str(generation_number))
    print_generation(population.get_schedules())
    print_schedule_as_table(population.get_schedules()[0], TIMES)


def plot_diagram(conflicts):
    plt.plot(conflicts)
    plt.ylabel("Number of Conflicts")
    plt.yticks(np.arange(0, conflicts[0] + 1, step=1))
    plt.xlabel("Generations")
    plt.Text("NUMBER_OF_ELITE_LECTURES: " + str(NUMBER_OF_ELITE_LECTURES))
    plt.Text("TOURNAMENT_SELECTION_SIZE: " + str(TOURNAMENT_SELECTION_SIZE))
    plt.Text("MUTATION_RATE: " + str(MUTATION_RATE))
    plt.Text("POPULATION_SIZE: " + str(POPULATION_SIZE))
    plt.show()


def print_stats(generation_number, conflicts, data):
    print("\n")
    print("Required Generations: " + str(generation_number))
    print("--")
    print("Used Inputs:")
    print("Number of Docents: " + str(len(data.get_docents())))
    print("Number of Time Slots: " + str(len(data.get_meeting_times())))
    print("Number of Courses: " + str(len(data.get_courses())))
    print("--")
    print("Parameters for the Genetic Algorithm:")
    print("NUMBER_OF_ELITE_LECTURES: " + str(NUMBER_OF_ELITE_LECTURES))
    print("TOURNAMENT_SELECTION_SIZE: " + str(TOURNAMENT_SELECTION_SIZE))
    print("MUTATION_RATE: " + str(MUTATION_RATE))
    print("POPULATION_SIZE: " + str(POPULATION_SIZE))
    print(conflicts)
    print("--")
    # plot_diagram(conflicts)


def print_available_data(data):
    print_courses(data.get_courses())
    print_docents(data.get_docents())
    print_room(data.get_rooms())
    print_meeting_times(data.get_meeting_times())