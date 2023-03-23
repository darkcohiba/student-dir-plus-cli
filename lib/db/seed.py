from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from models import Student, Teacher


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///studentDir.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # clear database
    session.query(Student).delete()
    session.query(Teacher).delete()

    print("Seeding teachers...")
    teachers = []
    sam = Teacher(
        teacher_id = 1,
        first_name = 'Sam',
        last_name = 'Waters'
    )
    teachers.append(sam)
    stephen = Teacher(
        teacher_id = 2,
        first_name = 'Stephen',
        last_name = 'Lamp'
    )
    teachers.append(stephen)

    yesenia = Teacher(
        teacher_id = 3,
        first_name = 'Yes Queen',
        last_name = 'Crown'
    )
    teachers.append(stephen)

    session.add_all(teachers)
    session.commit()

    print("Finished seeding Teachers...")
    print("Seeding students...")

    # teachers = session.query(Teacher).first()
    students = []
    student_ids = list(range(1, 11))
    student_first_names = ["Chase", "Max", "Yesenia", "Josh"]
    student_last_names = ["Walsh", "Welsh", "Ray", "Rey"]
    for teacher in teachers:
        # for i in range(random.randint(3, 5)):
        student = Student(
            student_id=student_ids[0],
            first_name=random.choice(student_first_names),
            last_name=random.choice(student_last_names),
            teacher_id=teacher.teacher_id,
        )
        student_ids.remove(student.student_id)
        student_first_names.remove(student.first_name)
        student_last_names.remove(student.last_name)
        students.append(student)
        session.add(student)
        session.commit()


    # chase = Student(
    #     student_id = 1,
    #     first_name = 'Chase',
    #     last_name = 'Walsh',
    #     teacher_id = 1
    # )

    # seth = Student(
    #     student_id = 1,
    #     first_name = 'Chase',
    #     last_name = 'Walsh',
    #     teacher_id = 2
    # )

    # students = [chase, seth]

    # session.add_all(teachers)
    # session.add_all(students)

    # session.add(chase)
    # session.commit()

    # print(session.query(Teacher).first)



    # session adding commands
    # session.bulk_save_objects(reviews)
    # session.commit()
    # session.close()


