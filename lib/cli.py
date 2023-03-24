from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Teacher, Student

engine = create_engine('sqlite:///db/studentDir.db')
session = sessionmaker(bind=engine)()

def create_new_teacher(fname, lname, id):
    new_teacher = Teacher(
        teacher_id = id,
        first_name = fname,
        last_name = lname,
    )
    session.add(new_teacher)
    session.commit()

def create_new_student(fname, lname, id):
    new_student = Student(
    )
    session.add(new_student)
    session.commit()

if __name__ == '__main__':

    print("Hello, welcome to our student and teacher database!")
    entry_type = input("Are you entering a new student or teacher? (S/T): ").lower()
    if entry_type == 't':
        teachers = session.query(Teacher).all()
        id = int(len(teachers) + 1)
        first_name = input('What is your first name')
        last_name = input('What is your last name')
        create_new_teacher(first_name, last_name, id)
    elif entry_type == 's':
        students = session.query(Student).all()
        id = int(len(students) + 1)
        first_name = input('What is your first name')
        last_name = input('What is your last name')
        teacher_id = int(input("What is your teacher's id"))
        teacher = session.query(Teacher).filter(Teacher.id == teacher_id).first()
        print(teacher)

        # create_new_teacher(first_name, last_name, teacher_id, id)


