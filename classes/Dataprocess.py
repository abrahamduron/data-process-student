from classes.Careers import Careers
from classes.DbMongo import DbMongo

class Dataprocess:

    def __init__(self, data):
        client, db = DbMongo.getDB()
        self.__data = data
        self.__collection = "career_students"
        self.carreras = []

    def create_careers(self, data):
        for e in data:
            temp_carreras = Careers(e['carrera'])
            self.carreras.append(temp_carreras)

    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        return True
    def create_students(self):
        ## Do something to create students on your mongodb collection using __data
        return True
    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        return True