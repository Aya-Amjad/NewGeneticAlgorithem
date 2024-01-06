from constants import TIMES

class Lecture:
    def __init__(self, id, course, TIMES=None, docent=None, room=None):
        self._id = id
        self._course = course
        self._docent = docent
        self._MEETING_TIMES = TIMES
        self._room = room

    def get_id(self): return self._id

    def get_course(self): return self._course

    def get_docent(self): return self._docent

    def get_meeting_time(self): return self._MEETING_TIMES

    def get_room(self): return self._room

    def set_docent(self, docent): self._docent = docent

    def set_room(self, room): self._room = room

    def set_meeting_time(self, TIMES): self._MEETING_TIMES = TIMES

    def __str__(self):
        return (
            str(self._course.get_number()) + ", " +
            str(self._room.get_number()) + ", " +
            str(self._docent.get_id()) + ", " +
            str(self._MEETING_TIMES)
        )