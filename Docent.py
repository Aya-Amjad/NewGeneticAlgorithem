class Docent:
    def __init__(self, id, name, min_hours, max_hours, start_time=None):
        self._id = id
        self._name = name
        self._min_hours = min_hours
        self._max_hours = max_hours
        self._start_time = start_time  # حقل وقت البداية (اختياري)
        self._assigned_hours = 0
        self._assigned_course_hours = 0
        self._available_times = []  # قائمة الأوقات المتاحة للدكتور

    def add_available_time(self, time):
        self._available_times.append(time)

    def get_available_times(self):
        return self._available_times

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_min_hours(self):
        return self._min_hours

    def get_max_hours(self):
        return self._max_hours

    def get_start_time(self):
        return self._start_time

    def set_start_time(self, start_time):
        self._start_time = start_time

    def is_available(self, meeting_time, course_hours):
        if meeting_time is not None and meeting_time.get_time() not in self._available_times:
            return False
        if self._assigned_hours + course_hours <= self._max_hours:
            return True
        else:
            return False

    def has_start_time_preference(self):
        return self._start_time is not None

    def get_assigned_hours(self):
        return self._assigned_hours

    def add_assigned_hours(self, hours):
        self._assigned_hours += hours

    def reduce_assigned_hours(self, hours):
        self._assigned_hours -= hours

    def reduce_max_hours(self, hours):
        self._max_hours -= hours
        self._assigned_hours += hours

    def add_assigned_course_hours(self, hours):
        self._assigned_course_hours += hours

    def start_time_to_number(self):
        # تحويل وقت البداية إلى رقم، على سبيل المثال: "10:30 AM" يتحول إلى 10.5
        if self._start_time is not None:
            start_time_parts = self._start_time.split()
            time_parts = start_time_parts[0].split(':')
            hours = int(time_parts[0])
            minutes = int(time_parts[1])

            if start_time_parts[1].lower() == 'pm' and hours != 12:
                hours += 12

            return hours + minutes / 60.0
        else:
            return None

    def __str__(self):
        return f"{self._name}, Start Time: {self._start_time if self._start_time is not None else 'Not specified'}"