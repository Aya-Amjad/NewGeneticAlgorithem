import random as rnd
from Lecture import Lecture
from Course import Course
import math
from Docent import Docent
from Room import Room
from constants import get_start_time, get_end_time, get_days

valid_day_combinations = {
    0: [["Sunday"], ["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"]],
    1: [["Sunday"], ["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"]],
    2: [["Sunday", "Tuesday"], ["Sunday", "Thursday"], ["Tuesday", "Thursday"]],
    3: [["Sunday", "Tuesday", "Thursday"], ["Monday", "Wednesday"]],
    4: [["Sunday", "Tuesday", "Thursday"], ["Monday", "Wednesday"]]
}
TIMES = [
            ["MT1", ["Sunday", "Tuesday", "Thursday"], "08:00", "09:00"],
            ["MT2", ["Sunday", "Tuesday", "Thursday"], "09:00", "10:00"],
            ["MT3", ["Sunday", "Tuesday", "Thursday"], "10:00", "11:00"],
            ["MT4", ["Sunday", "Tuesday", "Thursday"], "11:00", "12:00"],
            ["MT5", ["Sunday", "Tuesday", "Thursday"], "12:00", "13:00"],
            ["MT6", ["Sunday", "Tuesday", "Thursday"], "13:00", "14:00"],
            ["MT7", ["Monday", "Wednesday"], "08:00", "09:30"],
            ["MT8", ["Monday", "Wednesday"], "09:30", "11:00"],
            ["MT9", ["Monday", "Wednesday"], "11:00", "12:30"],
            ["MT10", ["Sunday"], "08:00", "10:00"],
            ["MT11", ["Sunday"], "10:00", "12:00"],
            ["MT12", ["Sunday"], "12:00", "14:00"],
            ["MT13", ["Monday"], "08:00", "10:00"],
            ["MT14", ["Monday"], "10:00", "12:00"],
            ["MT15", ["Monday"], "12:00", "14:00"],
            ["MT16", ["Tuesday"], "08:00", "10:00"],
            ["MT17", ["Tuesday"], "10:00", "12:00"],
            ["MT18", ["Tuesday"], "12:00", "14:00"],
            ["MT19", ["Wednesday"], "08:00", "10:00"],
            ["MT20", ["Wednesday"], "10:00", "12:00"],
            ["MT21", ["Wednesday"], "12:00", "14:00"],
            ["MT22", ["Thursday"], "08:00", "10:00"],
            ["MT23", ["Thursday"], "10:00", "12:00"],
            ["MT24", ["Thursday"], "12:00", "14:00"],
            ["MT25", ["Sunday", "Tuesday"], "08:00", "09:00"],
            ["MT26", ["Sunday", "Tuesday"], "09:00", "10:00"],
            ["MT27", ["Sunday", "Tuesday"], "10:00", "11:00"],
            ["MT28", ["Sunday", "Tuesday"], "11:00", "12:00"],
            ["MT29", ["Sunday", "Tuesday"], "12:00", "13:00"],
            ["MT30", ["Sunday", "Tuesday"], "13:00", "14:00"],
            ["MT31", ["Tuesday", "Thursday"], "08:00", "09:00"],
            ["MT32", ["Tuesday", "Thursday"], "09:00", "10:00"],
            ["MT34", ["Tuesday", "Thursday"], "10:00", "11:00"],
            ["MT35", ["Tuesday", "Thursday"], "11:00", "12:00"],
            ["MT36", ["Tuesday", "Thursday"], "12:00", "13:00"],
            ["MT37", ["Tuesday", "Thursday"], "13:00", "14:00"],
            ["MT38", ["Sunday", "Thursday"], "08:00", "09:00"],
            ["MT39", ["Sunday", "Thursday"], "09:00", "10:00"],
            ["MT40", ["Sunday", "Thursday"], "10:00", "11:00"],
            ["MT41", ["Sunday", "Thursday"], "11:00", "12:00"],
            ["MT42", ["Sunday", "Thursday"], "12:00", "13:00"],
            ["MT43", ["Sunday", "Thursday"], "13:00", "14:00"]
            ]
class Schedule:
    def _init_(self, data):
        self._data = data
        self._lectures = []
        self._number_of_conflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._is_fitness_changed = True

    def get_lectures(self):
        self._is_fitness_changed = True
        return self._lectures

    def get_number_of_conflicts(self):
        return self._number_of_conflicts

    def get_fitness(self):
        if self._is_fitness_changed:
            self._fitness = self.calculate_fitness()
            self._is_fitness_changed = False
        return self._fitness

    def initialize(self):
        courses = self._data.get_courses()
        rooms = self._data.get_rooms()

        for course in courses:
            num_sections = math.ceil(course.get_number_of_students() / course.get_max_students_per_room())

            for _ in range(num_sections):
                days = rnd.choice(valid_day_combinations[course.get_number_of_hours()])
                available_meeting_times = [mt for mt in TIMES if set(days) == set(mt[1])]

                requires_projector = course.get_requires_projector()
                suitable_rooms = [room for room in rooms if room.get_seating_capacity() >= course.get_max_students_per_room()]

                # Modify suitable_rooms based on the number of hours and projector requirement
                if course.get_number_of_hours() == 1:
                    if requires_projector:
                        suitable_rooms = [room for room in suitable_rooms if room.get_room_type() == "عملي" and room.get_has_projector()]
                    else:
                        suitable_rooms = [room for room in suitable_rooms if room.get_room_type() == "عملي"]
                else:
                    if requires_projector:
                        suitable_rooms = [room for room in suitable_rooms if room.get_room_type() == "نظري" and room.get_has_projector()]
                    else:
                        suitable_rooms = [room for room in suitable_rooms if room.get_room_type() == "نظري"]

                # Additional condition to prevent "عملي" rooms for courses with more than 1 hour
                if course.get_number_of_hours() > 1 and suitable_rooms:
                    suitable_rooms = [room for room in suitable_rooms if room.get_room_type() != "عملي"]

                if not suitable_rooms:
                    suitable_rooms = [Room("unknown", course.get_max_students_per_room(), "نظري", False)]

                remaining_capacity = min(course.get_max_students_per_room(), course.get_number_of_students())
                course.set_number_of_students(course.get_number_of_students() - remaining_capacity)

                meeting_time = None

                # تعريف مجموعة لتتبع الدكاترة الذين لديهم عدد ساعات أقل من min_hours
                docents_with_less_hours = [docent for docent in course.get_docents() if docent.get_assigned_hours() < docent.get_min_hours() ]


                # في حال وجود دكتور لديه عدد ساعات أقل من min_hours
                if docents_with_less_hours:
                    suitable_docents = docents_with_less_hours
                else:
                    suitable_docents = [docent for docent in course.get_docents() if docent.is_available(None, course.get_number_of_hours()) ]

                # Sort the suitable docents based on the difference between their min and max hours
                #suitable_docents.sort(key=lambda docent: docent.get_assigned_hours(), reverse=True)
                courses.sort(key=lambda course: course.get_number_of_hours(), reverse=True)
                suitable_docents.sort(key=lambda docent: (-docent.get_assigned_hours(),docent.get_assigned_hours() < docent.get_min_hours(),-abs(docent.get_min_hours() - docent.get_assigned_hours())), reverse=True)

                while available_meeting_times:
                    meeting_time = rnd.choice(available_meeting_times)

                    if suitable_rooms:
                        new_room = rnd.choice(suitable_rooms)
                        new_lecture = Lecture(self._classNumb, course, meeting_time)
                        new_lecture.set_room(new_room)

                        if not self.has_room_conflict(new_room, meeting_time, days):
                            if suitable_docents:
                                new_lecture.set_docent(suitable_docents[0])
                                suitable_docents[0].add_assigned_hours(course.get_number_of_hours())
                                suitable_docents[0].add_assigned_course_hours(course.get_number_of_hours())
                                # Remove the assigned docent from the list if their hours match
                                if suitable_docents[0].get_min_hours() == suitable_docents[0].get_max_hours():
                                    suitable_docents.pop(0)
                                
                            else:
                                new_lecture.set_docent(Docent("NULL", "NULL", 0, 0))

                            self._lectures.append(new_lecture)
                            self._classNumb += 1
                            break
                    else:
                        available_meeting_times.remove(meeting_time)

        return self

    def get_days(meeting_time):
        return meeting_time[1]

    def get_start_time(meeting_time):
        return meeting_time[2]

    def get_end_time(meeting_time):
        return meeting_time[3]


    def has_room_conflict(self, room, meeting_time, days):
        for existing_lecture in self._lectures:
            existing_start = get_start_time(existing_lecture.get_meeting_time())
            existing_end = get_end_time(existing_lecture.get_meeting_time())

            meeting_start = get_start_time(meeting_time)
            meeting_end = get_end_time(meeting_time)

            if (set(get_days(existing_lecture.get_meeting_time())) & set(days)) and \
                    int(existing_end.split(':')[0]) > int(meeting_start.split(':')[0]) and \
                    int(existing_start.split(':')[0]) < int(meeting_end.split(':')[0]) and \
                    existing_lecture.get_room() == room:
                return True

        return False

    def calculate_fitness(self):
        self._number_of_conflicts = 0
        classes = self.get_lectures()
        for i in range(0, len(classes)):
            seating_capacity = classes[i].get_room().get_seating_capacity()
            number_of_students = classes[i].get_course().get_number_of_students()
            if seating_capacity < number_of_students:
                self._number_of_conflicts += 1
            for j in range(0, len(classes)):
                if j >= i:
                    if (classes[i].get_meeting_time() == classes[j].get_meeting_time() and
                            classes[i].get_id() != classes[j].get_id()):
                        if classes[i].get_room() == classes[j].get_room():
                            self._number_of_conflicts += 1
                        if classes[i].get_docent() == classes[j].get_docent():
                            self._number_of_conflicts += 1
                        if classes[i].get_course() == classes[j].get_course():
                            self._number_of_conflicts += 1
        return 1 / (1.0 * self._number_of_conflicts + 1)

    def __str__(self):
        return_value = ""

        if self._lectures:
            for i in range(0, len(self._lectures) - 1):
                return_value += str(self._lectures[i]) + " | "
            return_value += str(self._lectures[-1])

        return return_value