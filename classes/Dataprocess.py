from classes.Careers import Careers
class Dataprocess:

    def __init__(self, data):
        self.__data = data
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