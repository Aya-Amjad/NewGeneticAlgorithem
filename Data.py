from sqlalchemy import create_engine, Column, String, Integer, MetaData, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from MeetingTime import MeetingTime

Base = declarative_base()



class Docent(Base):
    __tablename__ = 'mydatabase_professor'
    id = Column(String, primary_key=True)
    name = Column(String)  # يجب أن يكون هنا
    min_hours = Column(Integer)
    max_hours = Column(Integer)
class Course(Base):
    __tablename__ = 'mydatabase_course'
    code = Column(Integer, primary_key=True)
    name = Column(String)
    number_of_students = Column(Integer)
    number_of_hours = Column(Integer)
    max_students_per_room = Column(Integer)
    requires_projector = Column(Boolean)

class Room(Base):
   __tablename__ = 'mydatabase_room'
   room_number = Column(String, primary_key=True)
   capacity = Column(Integer)  # يجب أن يكون هنا
   room_type = Column(String)
   has_projector = Column(Boolean)

class Data:
    meeting_times = [
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
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData()
        self.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_docents(self):
        return self.session.query(Docent).all()
    
    def get_courses(self):
        return self.session.query(Course).all()
    
    def get_rooms(self):
        return self.session.query(Room).all()
   

    def close_session(self):
        self.session.close()

# تحديث البيانات
data = Data(db_url="postgresql://postgres:123456789@localhost:5432/DB")

docents=data.get_docents()
for docent in docents:
    print(f"prof ID: {docent.id}, Name: {docent.name} , min_hours:{docent.min_hours}, number_of_hours:{docent.max_hours}")

courses = data.get_courses()
for course in courses:
    print(f"Course ID: {course.code} Name: {course.name} , number_of_students:{course.number_of_students}, number_of_hours:{course.number_of_hours}, max_students_per_room:{course.max_students_per_room}, requires_projector:{course.requires_projector}")


rooms=data.get_rooms()
for room in rooms:
    print(f"room_number:{room.room_number}, capacity:{room.capacity}, room_type:{room.room_type}, has_projector:{room.has_projector}")
   
    def get_docents(self):
        return self._docents

    def get_rooms(self):
        return self._rooms

    def get_courses(self):
        return self._courses


    



# إغلاق الجلسة عند الانتهاء
data.close_session()
