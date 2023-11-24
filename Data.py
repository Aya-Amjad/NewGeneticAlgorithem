from Course import Course
from Docent import Docent
from MeetingTime import MeetingTime
from Room import Room

class Data:
    def __init__(self):
        rooms = [
            ["R1", 60, "نظري", True],
            ["R2", 18, "عملي", False],
            ["R3", 20, "عملي", False],
            ["R4", 30, "نظري", True],
            ["R5", 40, "عملي", True],
            ["R6", 40, "نظري", True],
            ["R7", 30, "نظري", True],
            ["R8", 60, "عملي", False]
        ]
        meeting_times = [
            ["MT1", ["Sunday", "Tuesday", "Thursday"], "08:00 – 09:00"],
            ["MT2", ["Sunday", "Tuesday", "Thursday"], "09:00 – 10:00"],
            ["MT3", ["Sunday", "Tuesday", "Thursday"], "10:00 – 11:00"],
            ["MT4", ["Sunday", "Tuesday", "Thursday"], "11:00 – 12:00"],
            ["MT5", ["Sunday", "Tuesday", "Thursday"], "12:00 – 13:00"],
            ["MT6", ["Sunday", "Tuesday", "Thursday"], "13:00 – 14:00"],
            ["MT7", ["Monday", "Wednesday"], "08:00 – 09:30"],
            ["MT8", ["Monday", "Wednesday"], "09:30 – 11:00"],
            ["MT9", ["Monday", "Wednesday"], "11:00 – 12:30"],
            ["MT10", ["Sunday"], "08:00 – 10:00"],
            ["MT11", ["Sunday"], "10:00 – 12:00"],
            ["MT12", ["Sunday"], "12:00 – 14:00"],
            ["MT13", ["Monday"], "08:00 – 10:00"],
            ["MT14", ["Monday"], "10:00 – 12:00"],
            ["MT15", ["Monday"], "12:00 – 14:00"],
            ["MT16", ["Tuesday"], "08:00 – 10:00"],
            ["MT17", ["Tuesday"], "10:00 – 12:00"],
            ["MT18", ["Tuesday"], "12:00 – 14:00"],
            ["MT19", ["Wednesday"], "08:00 – 10:00"],
            ["MT20", ["Wednesday"], "10:00 – 12:00"],
            ["MT21", ["Wednesday"], "12:00 – 14:00"],
            ["MT22", ["Thursday"], "08:00 – 10:00"],
            ["MT23", ["Thursday"], "10:00 – 12:00"],
            ["MT24", ["Thursday"], "12:00 – 14:00"],
            ["MT25", ["Sunday", "Tuesday"], "08:00 – 09:00"],
            ["MT26", ["Sunday", "Tuesday"], "09:00 – 10:00"],
            ["MT27", ["Sunday", "Tuesday"], "10:00 – 11:00"],
            ["MT28", ["Sunday", "Tuesday"], "11:00 – 12:00"],
            ["MT29", ["Sunday", "Tuesday"], "12:00 – 13:00"],
            ["MT30", ["Sunday", "Tuesday"], "13:00 – 14:00"],
            ["MT31", ["Tuesday", "Thursday"], "08:00 – 09:00"],
            ["MT32", ["Tuesday", "Thursday"], "09:00 – 10:00"],
            ["MT34", ["Tuesday", "Thursday"], "10:00 – 11:00"],
            ["MT35", ["Tuesday", "Thursday"], "11:00 – 12:00"],
            ["MT36", ["Tuesday", "Thursday"], "12:00 – 13:00"],
            ["MT37", ["Tuesday", "Thursday"], "13:00 – 14:00"],
            ["MT38", ["Sunday", "Thursday"], "08:00 – 09:00"],
            ["MT39", ["Sunday", "Thursday"], "09:00 – 10:00"],
            ["MT40", ["Sunday", "Thursday"], "10:00 – 11:00"],
            ["MT41", ["Sunday", "Thursday"], "11:00 – 12:00"],
            ["MT42", ["Sunday", "Thursday"], "12:00 – 13:00"],
            ["MT43", ["Sunday", "Thursday"], "13:00 – 14:00"]
        ]

        docents = [
            ["HO", "Haneen,Obaid",6, 8],
            ["MO", "Mosad Obaid", 1, 3],
            ["AA", "Aya Amjad", 1, 3],
            ["RA", "Raneen,Abd", 6, 6],
            ["JA", "Jana,Ardah", 1,1],
            ["AO", "Aseel,Obaid", 2,2]
        ]

        self._rooms = []
        self._meeting_times = []
        self._docents = []
        self.fill_objects(rooms, meeting_times, docents)

        Course1 = Course("WB", "Web", [self.get_docent("HO")], 60, 3, 60, True)
        Course2 = Course("OR", "Networks", [self.get_docent("MO") ], 60, 3, 30, False)
        Course3 = Course("TT", "Data Mining", [self.get_docent("AO"), self.get_docent("HO")], 100, 2, 50, False)
        Course4 = Course("SIC", "French", [self.get_docent("AA"),self.get_docent("HO")], 140, 1, 40, True)
        Course5 = Course("CM", "Sensors", [self.get_docent("JA")], 40, 1, 15, False)
        Course6 = Course("MIC", "Signal ", [self.get_docent("RA"),self.get_docent("HO")], 34, 3, 18, True)

        self._courses = [Course1, Course2, Course3, Course4, Course5, Course6]


    def get_docents(self):
        return self._docents


    def get_rooms(self):
        return self._rooms

    def get_courses(self):
        return self._courses

    def get_meeting_times(self):
        return self._meeting_times

    def fill_objects(self, rooms, meeting_times, docents):
        for room in rooms:
            self._rooms.append(Room(room[0], room[1], room[2], room[3]))

        for time in meeting_times:
            self._meeting_times.append(MeetingTime(time[0], time[1], time[2]))

        for docent in docents:
            self._docents.append(Docent(docent[0], docent[1], docent[2], docent[3]))

    def get_docent(self, name):
        return next((docent for docent in self._docents if docent.get_id() == name), None)