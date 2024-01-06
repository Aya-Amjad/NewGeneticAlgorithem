# database_setup.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ClassSchedule(Base):
    __tablename__ = 'class_schedule'

    id = Column(Integer, primary_key=True)
    stunde_number = Column(Integer)
    course = Column(String)
    room_number = Column(String)
    doctor = Column(String)
    time_slot = Column(String)
    day = Column(String)
    
