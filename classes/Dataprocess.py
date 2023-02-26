from classes.Careers import Careers
class Dataprocess:

    def __init__(self, data):
        self.__data = data

    def create_careers(self, data):
        if data[180] in data:
            print("Name:", data[180])
        else:
            print("No such student!")

    def create_courses(self):
        ## Do something to create courses on your mongodb collection using __data
        return True
    def create_students(self):
        ## Do something to create students on your mongodb collection using __data
        return True
    def create_enrollments(self):
        ## Do something to create enrollments on your mongodb collection using __data
        return True