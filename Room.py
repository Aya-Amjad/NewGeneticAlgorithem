class Room:
    def __init__(self, room_number, seating_capacity, room_type, has_projector):
        self._room_number = room_number
        self._seating_capacity = seating_capacity
        self._room_type = room_type
        self._has_projector = has_projector

    def get_number(self):
        return self._room_number

    def has_projector(self):
        return self._has_projector

    def get_seating_capacity(self):
        return self._seating_capacity

    def get_room_type(self):
        return self._room_type

    def __str__(self):
        return f"{self._room_number} ({self._room_type})"