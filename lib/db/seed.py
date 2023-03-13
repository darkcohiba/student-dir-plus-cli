from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Student, Teacher


if __name__ == '__main__':
    
    engine = create_engine('sqlite:///studentDir.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # clear database
    # session.query(Student).delete()
    # session.query(Teacher).delete()

    print("Seeding teachers...")

    sam = Teacher(
        teacher_id = 1,
        first_name = 'Sam',
        last_name = 'Waters'
    )

    session.add(sam)
    print("Seeding students...")

    chase = Student(
        student_id = 1,
        first_name = 'Chase',
        last_name = 'Walsh',
        teacher_id = 1
    )

    session.add(chase)
    session.commit()

    # print(session.query(Teacher).first)



    # session adding commands
    # session.bulk_save_objects(reviews)
    # session.commit()
    # session.close()


