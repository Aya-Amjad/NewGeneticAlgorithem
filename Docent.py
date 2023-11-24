class Docent:
    def __init__(self, id, name, min_hours, max_hours):
        self._id = id
        self._name = name
        self._min_hours = min_hours
        self._max_hours = max_hours
        self._assigned_hours = 0  # تتبع الساعات المعينة للدكتور
        self._assigned_course_hours = 0  # تتبع الساعات المعينة للمواد
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_min_hours(self):
        return self._min_hours

    def get_max_hours(self):
        return self._max_hours    
    # الدالة المعدلة لتحقق من توفر الدكتور في وقت معين مع مقارنة عدد الساعات المعينة له للمواد
    def is_available(self, meeting_time, course_hours):
      return self._assigned_hours + course_hours <= self._max_hours
            # تحقق من توفر الدكتور في هذا الوقت
            # يمكنك إضافة المزيد من الشروط هنا إذا كنت بحاجة
        

    def get_assigned_hours(self):
        return self._assigned_hours
    def add_assigned_hours(self, hours):
        self._assigned_hours += hours
    def reduce_assigned_hours(self, hours):
        self._assigned_hours -= hours

    def reduce_max_hours(self, hours):
        self._max_hours -= hours
        self._assigned_hours += hours  # زيادة الساعات المعينة للدكتور

    def reduce_assigned_hours(self, hours):
        self._assigned_hours -= hours

    def add_assigned_course_hours(self, hours):
        self._assigned_course_hours += hours

    def __str__(self):
        return self._name