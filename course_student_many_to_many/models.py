from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
# Assoziationstabelle (M:N)

student_course = Table(
    'student_course', Base.metadata,
    Column('student_id',Integer, ForeignKey('students.id'),primary_key=True),# primary_key=True zusammengester PK
    Column('course_id',Integer, ForeignKey('courses.id'),primary_key=True)
)


class Student(Base):
    __tablename__="students"
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    courses= relationship('Course',secondary=student_course,back_populates='students', cascade="all" )# all, delete, 

class Course(Base):
    __tablename__="courses"
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    students= relationship('Student',secondary=student_course,back_populates='courses', cascade="all" )