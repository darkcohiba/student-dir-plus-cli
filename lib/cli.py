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

def create_new_student(fname, lname, teacher_id, student_id):
    new_student = Student(
        student_id=student_id,
        first_name=fname,
        last_name=lname,
        teacher_id=teacher_id.teacher_id,
    )
    session.add(new_student)
    session.commit()

def add_student_or_teacher():
    """function to add a student or teacher to the database"""
    entry_type = input("Are you entering a new student or teacher? (S/T): ").lower()
    if entry_type == 't':
        print("Enter the teacher data below:")
        teachers = list(session.query(Teacher).all())
        id = int((str(teachers[-1]))[4]) + 1
        first_name = input('What is your first name: ')
        last_name = input('What is your last name: ')
        create_new_teacher(first_name, last_name, id)
    elif entry_type == 's':
        print("Enter the student data below:")
        students = list(session.query(Student).all())
        id = int((str(students[-1]))[4]) + 1
        first_name = input('What is your first name: ')
        last_name = input('What is your last name: ')
        students_teacher = input("What is your teacher's first name: ")
        teacher = session.query(Teacher).filter(Teacher.first_name == students_teacher).first()
        print(teacher)
        create_new_student(first_name, last_name, teacher, id)

def remove_data():
    choice_type = input("Are you deleting a student or a teacher?  (student/teacher) : ").title()
    if choice_type == 'student':
        data_name = input(f'What is the first name of the {choice_type} you wish to remove: \n')
        session.query(Student).filter(Student.first_name == data_name).delete()
        session.commit()
    elif choice_type == 'teacher':
        data_name = input(f'What is the first name of the {choice_type} you wish to remove: \n')
        session.query(Teacher).filter(Teacher.first_name == data_name).delete()
        session.commit()

def view_data():
    choice_type = input("Do you want to view teachers or students? (student/teacher) : ").lower()
    if choice_type == 'teacher':
        teachers = session.query(Teacher).all()
        for teacher in teachers:
            print('{}, {} \n'.format(teacher.last_name, teacher.first_name))
    elif choice_type == 'student':
        students = session.query(Student).all()
        for student in students:
            print('{}, {}, id: {} \n'.format(student.last_name, student.first_name, student.student_id))



if __name__ == '__main__':

    print("Hello, welcome to our student and teacher database!")
    system_running = True
    while system_running:
        print("These are the services we offer: \n 1. Adding Students/Teachers \n 2. Viewing Students/Teachers \n 3. Removing Students/Teachers \n")
        option = int(input("Which service do you want, type the number that corresponds with the service: \n"))
        if option == 1:
            add_student_or_teacher()
            print("Thank you for adding to our database!")
        elif option == 2:
            view_data()
        elif option == 3:
            remove_data()
            print("Thank you for removing data from our database!")

