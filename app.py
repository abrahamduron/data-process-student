import pymongo
from classes import DATA, Dataprocess, DbMongo, Careers, Courses, Students, Enrollments
from dotenv import load_dotenv

def main():

    client, db = DbMongo.getDB()
##########################################
    Careers.delete_all(db)
    Courses.delete_all(db)
    Enrollments.delete_all(db)
    Students.delete_all(db)
#########################################
    pipeline = Dataprocess(DATA)
    print(pipeline)
    pipeline.create_careers(DATA)
    pipeline.create_students()
    pipeline.create_enrollments()

    print(DATA[1])

    return True

if __name__ == "__main__":
    load_dotenv()
    main()