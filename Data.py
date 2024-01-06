from sqlalchemy import create_engine, Column, String, Integer, MetaData, Boolean, ForeignKey,BIGINT,CHAR
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from constants import TIMES
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProfessorCourseAssociation(Base):
    __tablename__ = 'mydatabase_course_professors'
    id = Column(BIGINT, primary_key=True)
    professor_id = Column(BIGINT, ForeignKey('mydatabase_professor.id'))
    course_id = Column(BIGINT, ForeignKey('mydatabase_course.id'))

class ScheduleTable(Base):
    __tablename__ = 'schedule'
    id = Column(Integer, primary_key=True)
    doctor_name = Column(String)  # استخدم String بدلاً من Integer إذا كان اسم الطبيب هو نص
    course_name = Column(String)  # استخدم String بدلاً من Integer إذا كان اسم الدورة هو نص
    room_number = Column(String)  # استخدم String بدلاً من Integer إذا كان رقم الغرفة هو نص
    time_slot = Column(String)
    day = Column(String)
    
class Docent(Base):
    __tablename__ = 'mydatabase_professor'
    id = Column(BIGINT, primary_key=True)
    id_number = Column(BIGINT)
    name = Column(CHAR)
    min_hours = Column(Integer)
    max_hours = Column(Integer)
    courses = relationship("Course", secondary="mydatabase_course_professors", back_populates="professors")   
    def __init__(self, id, name, min_hours, max_hours, assigned_hours=None, assigned_course_hours=None):
        self.id = id
        self.name = name
        self.min_hours = min_hours
        self.max_hours = max_hours
        self._assigned_hours = 0  
        self._assigned_course_hours = 0 
    @property
    def assigned_hours(self):
        return getattr(self, '_assigned_hours', 0)
    @assigned_hours.setter
    def assigned_hours(self, value):
        self._assigned_hours = value
    @property
    def assigned_course_hours(self):
        return getattr(self, '_assigned_course_hours', 0)
    @assigned_course_hours.setter
    def assigned_course_hours(self, value):
        self._assigned_course_hours = value
    def get_assigned_hours(self):
        return self.assigned_hours
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_min_hours(self):
        return self.min_hours
    def get_max_hours(self):
        return self.max_hours
    def is_available(self, meeting_time, course_hours):
        return self.assigned_hours + course_hours <= self.max_hours            
    def add_assigned_hours(self, hours):
        self.assigned_hours += hours
    def reduce_assigned_hours(self, hours):
        self.assigned_hours -= hours
    def add_assigned_course_hours(self, hours):
        self.assigned_course_hours += hours
    def __str__(self):
        return f" Name: {self.name}"
   

class Course(Base):
    __tablename__ = 'mydatabase_course'
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String)
    name = Column(String)  
    number_of_students = Column(Integer)
    number_of_hours = Column(Integer)
    max_students_per_room = Column(Integer)
    requires_projector = Column(Boolean)
    professors = relationship("Docent", secondary="mydatabase_course_professors", back_populates="courses")
    def __init__(self, code, name, number_of_students, number_of_hours, max_students_per_room, requires_projector):
        self.code = code
        self.name = name
        self.number_of_students = number_of_students
        self.number_of_hours = number_of_hours
        self.max_students_per_room = max_students_per_room
        self.requires_projector = requires_projector
    def get_number(self):
        return self.code
    def get_max_students_per_room(self):
        return self.max_students_per_room
    def get_name(self):
        return self.name
    def get_docents(self):
        return self.professors 
    def get_number_of_students(self):
        return self.number_of_students
    def get_number_of_hours(self):
        return self.number_of_hours
    def set_number_of_students(self, new_number_of_students):
        self.number_of_students = new_number_of_students
    def get_requires_projector(self):
        return self.requires_projector
    def __str__(self):
        return f"{self.name} ({self.requires_projector})"

class Room(Base):
    __tablename__ = 'mydatabase_room'
    id = Column(Integer, primary_key=True)
    room_number = Column(String)
    capacity = Column(Integer)
    room_type = Column(Integer) 
    has_projector = Column(Boolean)
    def __init__(self, room_number, capacity, room_type, has_projector):
        self.room_number = room_number
        self.capacity = capacity
        self.room_type = room_type
        self.has_projector = bool(has_projector)
    def get_number(self):
        return self.room_number
    def get_seating_capacity(self):
        return self.capacity
    def get_room_type(self):
        return self.room_type
    def get_has_projector(self):
        return self.has_projector
    def __str__(self):
        return f"{self.room_number} ({self.room_type})"

class Data:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData()
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.TIMES = [
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
            ["MT43", ["Sunday", "Thursday"], "13:00", "14:00"],
            ["MT44", ["monday", "wednesday"], "08:00", "09:00"],
            ["MT45", ["monday", "wednesday"], "09:00", "10:00"],
            ["MT46", ["monday", "wednesday"], "10:00", "11:00"],
            ["MT47", ["monday", "wednesday"], "11:00", "12:00"],
            ["MT48", ["monday", "wednesday"], "12:00", "13:00"],
            ["MT49", ["monday", "wednesday"], "13:00", "14:00"]
            ]
        #self._MEETING_TIMES = []
        self._rooms = self.get_rooms()  # قم بإضافة هذا السطر لتحديث _rooms
        self._docents = self.get_docents()  # قم بإضافة هذا السطر لتحديث _docents
    def get_docents(self):
        return self.session.query(Docent).all()    
    def get_courses(self):
        return self.session.query(Course).all()    
    def get_rooms(self):
        return self.session.query(Room).all()    
    def get_meeting_times(self):
        return self.TIMES    
    def get_ProfessorCoursesAssociation(self):
        return self.session.query(ProfessorCourseAssociation).all()
    def close_session(self):
        self.session.close()
# تحديث البيانات
data = Data(db_url="postgresql://postgres:123456789@localhost:5432/DB")