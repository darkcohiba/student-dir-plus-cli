from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Teacher

engine = create_engine('sqlite:///db/studentDir.db')
session = sessionmaker(bind=engine)()


if __name__ == '__main__':
    


    teachers = session.query(Teacher).all()
    print(teachers)

