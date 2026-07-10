from database import Base, engine, session
from models import Student,Course
from crud import StudentRepository,CourseRepository
def main():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)# create table if not exists
    studentrepo = StudentRepository(session)
    courserepo = CourseRepository(session)
    
    s1= studentrepo.add_student("Ina")
    c1= courserepo.add_course("Python")
    c2= courserepo.add_course("Java")
    studentrepo.assign_course(s1.id,c1.id)
    studentrepo.assign_course(s1.id,c2.id)

   
if __name__=="__main__":
    main()
