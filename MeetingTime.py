class MeetingTime:
    def __init__(self, id, days, time, course=None):
        valid_day_combinations = {
            1: [["Sunday"], ["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"]],
            2: [["Sunday", "Tuesday"], ["Sunday", "Thursday"], ["Tuesday", "Thursday"]],
            3: [["Sunday", "Tuesday", "Thursday"], ["Monday", "Wednesday"]]
        }
        
        
        if course:
            if course.get_number_of_hours() == 1:
                valid_day_combinations = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
                    
            elif course.get_number_of_hours() == 2:
                valid_day_combinations = [["Sunday", "Tuesday"], ["Sunday", "Thursday"], ["Tuesday", "Thursday"]]
            elif course.get_number_of_hours() == 3:
                valid_day_combinations = [["Sunday", "Tuesday", "Thursday"], ["Monday", "Wednesday"]]
            else:
                raise ValueError("Invalid number of course hours. Must be either 1, 2, or 3.")

            # Check if the provided days are valid
            if days not in valid_day_combinations:
                raise ValueError("Invalid day or course hours combination.")

            self._id = id
            self._days = days
            self._time = time
            self._course = course
        else:
            self._id = id
            self._days = days
            self._time = time
            self._course = None

    def get_id(self):
        return self._id

    def get_days(self):
        return self._days
        

    def get_time(self):
        return self._time

    def get_course(self):
        return self._course