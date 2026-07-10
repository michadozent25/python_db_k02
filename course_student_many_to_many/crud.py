from models import Student, Course

class StudentRepository:
    def __init__(self,session):
        self.session =session
        

    def add_student(self,name:str):
        student = Student(name=name)
        self.session.add(student)
        self.session.commit()
        return student
    def assign_course(self, student_id: int, course_id: int) -> Student | None:
        """Verknüpft einen existierenden Student mit einem Course."""
        student = self.session.get(Student, student_id)
        course = self.session.get(Course, course_id)

        # Beziehung hinzufügen, wenn sie nicht schon besteht
        if course not in student.courses:
            student.courses.append(course)
            self.session.commit()
        return student
class CourseRepository:
    def __init__(self,session):
        self.session =session
    def add_course(self,name:str):
        course = Course(name=name)
        self.session.add(course)
        self.session.commit()
        return course