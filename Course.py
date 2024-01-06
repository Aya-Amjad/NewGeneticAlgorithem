class Course:
    def __init__(self, token, name, docents, number_of_students, number_of_hours, max_students_per_room, requires_projector):
        self._token = token
        self._name = name
        self._docents = docents
        self._number_of_students = number_of_students
        self._number_of_hours = number_of_hours
        self._max_students_per_room = max_students_per_room
        self._requires_projector = requires_projector  # Added requires_projector attribute

    def get_number(self):
        return self._token
    def get_docents(self):
        return self._docents

    def get_max_students_per_room(self):
        return self._max_students_per_room
    def get_token(self):
        return self._token
    def get_name(self):
        return self._name

    def get_docents(self):
        return self._docents
    
    def get_number_of_students(self):
        return self._number_of_students

    def get_number_of_hours(self):
        return self._number_of_hours

    def set_number_of_students(self, new_number_of_students):
        self._number_of_students = new_number_of_students

    def requires_projector(self):
        return self._requires_projector

    def __str__(self):
        return self._name